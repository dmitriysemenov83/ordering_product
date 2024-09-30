from rest_framework.pagination import PageNumberPagination


class ProductPaginator(PageNumberPagination):
    page_size = 10

class CategoryPaginator(PageNumberPagination):
    page_size = 5