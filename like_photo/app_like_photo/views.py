import datetime

from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from like_photo.settings import EMAIL_SENDER

from .forms import FormForCreate
from .models import Post

# Create your views here.


class PostListView(ListView):
    model = Post
    template_name = "app_like_photo/main.html"
    context_object_name = "posts"

    def get_queryset(self):
        # Получаем только активные объекты
        return Post.objects.filter(is_active=True)


class PostDetailView(DetailView):
    model = Post
    template_name = "app_like_photo/post.html"
    context_object_name = "post"

    def created_at_post(self):
        created_at_post = self.object.created_at
        time = datetime.date.today() - created_at_post
        if time.days == 0:
            result = "сегодня"
        elif time.days == 1:
            result = "вчера"
        else:
            result = f"{time.days} дней(дня) назад"
        return result

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["created_at_post"] = self.created_at_post()
        return context

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        if self.object.views_count == 100:
            send_mail(
                "от like_photo",
                f"Поздравляем, ваша публикация {self.object.header} набрала 100 просмотров",
                EMAIL_SENDER,
                ["serega94nn@yandex.ru"],
            )
        return self.object


class PostCreateView(CreateView):
    model = Post
    form_class = FormForCreate
    template_name = "app_like_photo/form_add_post.html"
    success_url = reverse_lazy("app_like_photo:main_views")


class PostUpdateView(UpdateView):
    model = Post
    form_class = FormForCreate
    template_name = "app_like_photo/form_add_post.html"

    def get_success_url(self):
        return reverse_lazy("app_like_photo:post_views", args=[self.kwargs.get("pk")])


class PostDeleteView(DeleteView):
    model = Post
    template_name = "app_like_photo/delete_post.html"
    success_url = reverse_lazy("app_like_photo:main_views")
