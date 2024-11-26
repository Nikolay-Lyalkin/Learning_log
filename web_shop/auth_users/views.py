from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.core.mail import send_mail
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView

from .forms import CustomLoginForm, CustomUserCreationForm


class RegisterView(CreateView):
    template_name = "auth_users/register.html"
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("catalog:home_views")

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        self.send_welcome_email(user.email, user.password)
        return super().form_valid(form)

    def send_welcome_email(self, user_email, user_password):
        subject = "Добро пожаловать в наш сервис"
        message = f"Спасибо, что зарегистрировались в нашем сервисе!"
        from_email = "serega94nn@yandex.ru"
        recipient_list = [user_email]
        send_mail(subject, message, from_email, recipient_list)


class UserLoginView(LoginView):
    form_class = CustomLoginForm
    template_name = "auth_users/login.html"
    success_url = reverse_lazy("catalog:home_views")
