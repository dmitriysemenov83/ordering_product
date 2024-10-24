from rest_framework import serializers

from orders.models import Order


class OrderSerializer(serializers.ModelSerializer):
    order_amount = serializers.SerializerMethodField()
    product_name = serializers.ReadOnlyField(source='product.title')

    class Meta:
        model = Order
        fields = ('id','user', 'product','product_name', 'quantity', 'created_at',
                  'updated_at', 'status', 'order_amount')
        read_only_fields = ('id', 'user','product_name', 'created_at', 'updated_at', 'status', 'order_amount')

    @staticmethod
    def get_order_amount(obj):
        order_amount = obj.quantity * obj.product.price * (1 - obj.product.discount / 100)
        return format(order_amount, '.2f')