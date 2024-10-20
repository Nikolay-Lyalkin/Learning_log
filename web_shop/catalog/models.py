from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Наименование категории")
    description = models.TextField(verbose_name="Описание")

    class Meta:
        db_table = "categories"


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="Наименование продукта")
    description = models.CharField(max_length=1000, verbose_name="Описание")
    image = models.ImageField(upload_to="photos/")
    category = models.ForeignKey(
        Category, on_delete=models.DO_NOTHING, related_name="products", max_length=100, verbose_name="Категория"
    )
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        ordering = ["category"]
        db_table = "products"


class Contact(models.Model):
    phone_number = models.CharField(max_length=12)
    email = models.EmailField()
    address = models.TextField()

    class Meta:
        db_table = "contacts"
