from rest_framework.test import APITestCase
from rest_framework.reverse import reverse
from rest_framework import status

from orders.models import Order
from products.models import Product, Category
from users.models import User


class OrderTestCase(APITestCase):

    def setUp(self):
        # Создаем пользователя для тестов
        self.user = User.objects.create(
            email='test@example.com',
            is_active=True
        )
        self.user.set_password('test_password')
        self.user.save()
        self.client.force_authenticate(user=self.user)
        # Создаем категорию для тестов
        self.category = Category.objects.create(
            name='Test Category',
            description='Test category description'
        )

        # Создаем товар для тестов
        self.product = Product.objects.create(
            title='Test Product',
            description='Test product description',
            price=100,
            discount=0,
            quantity=10,
            category=self.category
        )
        # Создаем заказ для тестов
        self.order = Order.objects.create(
            user=self.user,
            product=self.product
        )

    def test_get_order(self):

        response = self.client.get(
            reverse('orders:orders_list')
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_orders(self):
        response = self.client.get(
            reverse(
                'orders:order_retrieve',
                kwargs={'pk': self.order.id})
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_staff_orders(self):
        self.user.is_staff = True
        self.user.save()

        response = self.client.get(
            reverse('orders:staff_list')
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_order(self):
        data = {
            'user': self.user.id,
            'product': self.product.id,
            'quantity': 2,
        }

        response = self.client.post(
            reverse('orders:order_create'), data=data
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_order(self):
        data = {
            'user': self.user.id,
            'product': self.product.id,
            'quantity': 3
        }
        response = self.client.put(
            reverse(
                'orders:order_update',
                kwargs={'pk': self.order.id}), data=data
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_order(self):
        response = self.client.delete(
            reverse(
                'orders:order_delete',
                kwargs={'pk': self.order.id})
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)