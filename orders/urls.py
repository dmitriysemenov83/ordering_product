from django.urls import path, include
from orders.apps import OrdersConfig
from orders.views import OrderListAPIView, OrderCreateAPIView, OrderRetrieveAPIView, OrderUpdateAPIView, \
    OrderDeleteAPIView, StaffListAPIView

app_name = OrdersConfig.name

urlpatterns = [
    path('', OrderListAPIView.as_view(), name='orders_list'),
    path('staff/', StaffListAPIView.as_view(), name='staff_list'),
    path('create/', OrderCreateAPIView.as_view(), name='order_create'),
    path('retrieve/<int:pk>/', OrderRetrieveAPIView.as_view(), name='order_retrieve'),
    path('update/<int:pk>/', OrderUpdateAPIView.as_view(), name='order_update'),
    path('delete/<int:pk>/', OrderDeleteAPIView.as_view(), name='order_delete'),
]