from django.urls import path

from . import views

app_name = "catalog"

urlpatterns = [
    path("home_views/", views.ProductListView.as_view(), name="home_views"),
    path("contact_views/", views.ContactTemplateView.as_view(), name="contact_views"),
    path("category_views/", views.CategoryListView.as_view(), name="category_views"),
    path("catalog_views/", views.CatalogProductListView.as_view(), name="catalog_views"),
    path("product_views/<int:pk>/", views.ProductDetailView.as_view(), name="product_views"),
    path("add_product_views/", views.ProductCreateView.as_view(), name="add_product_views"),
    path("update_product_views/<int:pk>/", views.ProductUpdateView.as_view(), name="update_product_views"),
    path(
        "product_views/<int:pk>/delete_product_views/", views.ProductDeleteView.as_view(), name="delete_product_views"
    ),
    path("unauthorized_user_views/", views.UnauthorizedUserListView.as_view(), name="unauthorized_user_views"),
    path("profile_views/<int:pk>/", views.ProfileDetailView.as_view(), name="profile_views"),
    path("update_profile_views/<int:pk>/", views.ProfileUpdateView.as_view(), name="update_profile_views"),
    path("popup_question_views/<int:pk>/", views.ProfilePopupTemplateView.as_view(), name="popup_question_views"),
    path(
        "unpublished_product_views/<int:pk>/", views.UnpublishedProductView.as_view(), name="unpublished_product_views"
    ),
]
