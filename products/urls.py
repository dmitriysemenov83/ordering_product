from django.urls import path, include

from products.apps import ProductsConfig
from rest_framework.routers import DefaultRouter

from products.views import ProductViewSet, CategoryViewSet

app_name = ProductsConfig.name

pr_router = DefaultRouter()
pr_router.register(r'products', ProductViewSet, basename='products')
cat_router = DefaultRouter()
cat_router.register(r'category', CategoryViewSet, basename='category')

urlpatterns = [
    path('', include(pr_router.urls)),
    path('', include(cat_router.urls)),

]