from django.core.cache import cache

from .models import Category, Product


class CategoryService:

    @staticmethod
    def get_product_in_category(category_id):
        products = Product.objects.filter(category_id=category_id)
        products = [product for product in products if product.is_active == True]
        return products
