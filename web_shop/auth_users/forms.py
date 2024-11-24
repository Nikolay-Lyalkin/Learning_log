from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django import forms
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(label="Никнейм", max_length=20, widget=forms.TextInput(attrs={"class": "form-control", "style": "width: 400px"}))
    email = forms.EmailField(label="Электронная почта", widget=forms.EmailInput(attrs={"class": "form-control", "style": "width: 400px"}))
    password1 = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={"class": "form-control", "style": "width: 400px"}))
    password2 = forms.CharField(label="Повторите пароль", widget=forms.PasswordInput(attrs={"class": "form-control", "style": "width: 400px"}))
    phone_number = forms.CharField(label="Номер телефона", max_length=15, required=False, help_text='Необязательное поле. Введите ваш номер телефона.', widget=forms.NumberInput(attrs={"class": "form-control", "style": "width: 400px"}))

    class Meta:
        model = CustomUser
        fields = ("username", "email", "password1", "password2")


class CustomLoginForm(AuthenticationForm):
    username = forms.EmailField(label="Электронная почта", widget=forms.EmailInput(attrs={"class": "form-control", "style": "width: 400px"}))
    password = forms.CharField(label="Повторите пароль", widget=forms.PasswordInput(attrs={"class": "form-control", "style": "width: 400px"}))

    class Meta:
        model = CustomUser
        fields = ("email", "password")
