from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, serializers
from rest_framework.permissions import IsAuthenticated

from orders.models import Order
from orders.paginators import OrderPagination
from orders.permissions import IsOwnerOrStaff, IsUserOnStaff
from orders.serializers import OrderSerializer
from products.models import Product


class OrderCreateAPIView(generics.CreateAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):

        product_id = self.request.data.get('product')
        quantity = serializer.validated_data.get('quantity')

        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            raise serializers.ValidationError('Продукт не найден.')

        # Проверяем наличие достаточного количества товара
        if quantity > product.quantity:
            raise serializers.ValidationError('Недостаточно товара на складе.')

        # Уменьшаем количество товара на складе
        product.quantity -= quantity
        product.save()

        # Сохраняем заказ с текущим пользователем
        serializer.save(user=self.request.user)


class OrderListAPIView(generics.ListAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all().order_by('-created_at')
    permission_classes = [IsAuthenticated]
    pagination_class = OrderPagination
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filterset_fields = ('user', 'product')
    ordering_fields = ('created_at',)

    def get_queryset(self):
        queryset = self.queryset.filter(user=self.request.user)
        return queryset


class StaffListAPIView(generics.ListAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all().order_by('-created_at')
    permission_classes = [IsAuthenticated, IsUserOnStaff]
    pagination_class = OrderPagination
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filterset_fields = ('user', 'product')
    ordering_fields = ('created_at',)


class OrderRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    permission_classes = [IsAuthenticated]


class OrderUpdateAPIView(generics.UpdateAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerOrStaff]


class OrderDeleteAPIView(generics.DestroyAPIView):
    queryset = Order.objects.all()
    permission_classes = [IsAuthenticated]