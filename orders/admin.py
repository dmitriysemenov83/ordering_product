from django.contrib import admin

from orders.models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'product', 'quantity', 'created_at', 'updated_at' , 'status')
    search_fields = ('user', 'product')
    list_filter = ('status', 'created_at')