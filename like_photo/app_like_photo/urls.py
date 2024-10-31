from django.urls import path

from . import views

app_name = "app_like_photo"

urlpatterns = [
    path("main_views/", views.PostListView.as_view(), name="main_views"),
    path("post_views/<int:pk>/", views.PostDetailView.as_view(), name="post_views"),
    path("add_post_views/", views.PostCreateView.as_view(), name="add_post_views"),
    path("update_post_views/<int:pk>/", views.PostUpdateView.as_view(), name="update_post_views"),
    path("post_views/<int:pk>/delete_post_views/", views.PostDeleteView.as_view(), name="delete_post_views"),
]
