from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from orders.permissions import IsUserOnStaff
from products.models import Product, Category
from products.serializers import ProductSerializer, CategorySerializer
from products.paginators import ProductPaginator, CategoryPaginator


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    pagination_class = ProductPaginator

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            permission_classes = [IsAuthenticated, IsUserOnStaff]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    pagination_class = CategoryPaginator

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            permission_classes = [IsAuthenticated, IsUserOnStaff]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
