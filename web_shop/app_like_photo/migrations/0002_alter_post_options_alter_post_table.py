# Generated by Django 5.1.1 on 2024-10-27 22:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app_like_photo", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="post",
            options={"verbose_name": "пост", "verbose_name_plural": "посты"},
        ),
        migrations.AlterModelTable(
            name="post",
            table="posts",
        ),
    ]