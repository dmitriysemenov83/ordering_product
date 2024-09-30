from django.contrib import admin

from products.models import Product, Category

admin.site.site_header = 'Магазин товаров'
admin.site.site_title = 'Администрирование магазина'
admin.site.index_title = 'Панель управления магазином'


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'price', 'discount', 'image', 'quantity')
    search_fields = ('title', 'description')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at', 'updated_at')
    search_fields = ('name',)
