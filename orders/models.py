
from django.db import models

from products.models import Product
from users.models import User


class Order(models.Model):
    user = models.ForeignKey(User, related_name = 'user', on_delete=models.CASCADE, verbose_name='Пользователь')
    product = models.ForeignKey(Product, related_name = 'product', on_delete=models.CASCADE, verbose_name='Продукт')
    quantity = models.PositiveIntegerField(default=1, verbose_name='Количество')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    status = models.CharField(max_length=50, choices=[
        ('pending', 'Ожидает обработки'),
        ('completed', 'Завершен'),
        ('canceled', 'Отменен'),
    ], default='pending', verbose_name='Статус заказа')

    class Meta:
        db_table = 'orders'
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f'Заказ id={self.id} user={self.user.username} product={self.product.title}'


