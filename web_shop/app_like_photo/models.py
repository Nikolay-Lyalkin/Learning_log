from django.db import models

# Create your models here.


class Post(models.Model):
    header = models.CharField(max_length=100, verbose_name="Заголовок поста")
    content = models.CharField(max_length=1000, verbose_name="Описание")
    image = models.ImageField(upload_to="photos/", verbose_name="Изображение")
    created_at = models.DateField(auto_now_add=True, verbose_name="Дата создания")
    is_active = models.BooleanField(default=True)
    views_count = models.IntegerField(default=0, verbose_name="Количество просмотров")

    def __str__(self):
        return f"{self.header}"

    class Meta:
        verbose_name = "пост"
        verbose_name_plural = "посты"
        db_table = "posts"
