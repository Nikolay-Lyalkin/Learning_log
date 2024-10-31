from django import forms

from .models import Category, Product


class FormForCreate(forms.ModelForm):
    name = forms.CharField(
        label="Наименование", widget=forms.TextInput(attrs={"class": "form-control", "style": "width: 400px"})
    )
    description = forms.CharField(
        label="Описание", widget=forms.Textarea(attrs={"class": "form-control", "style": "height: 100px"})
    )
    image = forms.ImageField(label="Изображение", widget=forms.FileInput(attrs={"class": "form-control"}))
    category = forms.ModelChoiceField(
        label="Категория",
        queryset=Category.objects.all(),
        widget=forms.Select(attrs={"class": "form-select", "style": "width: 200px"}),
    )
    price = forms.DecimalField(
        label="Цена", widget=forms.TextInput(attrs={"class": "form-control", "style": "width: 200px"})
    )

    class Meta:
        model = Product
        fields = ["name", "description", "image", "category", "price"]
