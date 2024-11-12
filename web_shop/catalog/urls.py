from django.urls import path

from . import views

app_name = "catalog"

urlpatterns = [
    path("home_views/", views.ProductListView.as_view(), name="home_views"),
    path("contact_views/", views.ContactTemplateView.as_view(), name="contact_views"),
    path("category_views/", views.category_views, name="category_views"),
    path("catalog_views/", views.catalog_views, name="catalog_views"),
    path("product_views/<int:pk>/", views.ProductDetailView.as_view(), name="product_views"),
    path("add_product_views/", views.ProductCreateView.as_view(), name="add_product_views"),
    path("update_product_views/<int:pk>/", views.ProductUpdateView.as_view(), name="update_product_views"),
]
