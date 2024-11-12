from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator

from .models import Category, Product


def validate_words(value):
    """Валидация наименования и описания товара на запрещенные слова"""
    banned_words = ["казино", "криптовалюта", "крипта", "биржа", "дешево", "бесплатно", "обман", "полиция", "радар"]
    for banned_word in banned_words:
        if banned_word in value.lower():
            raise ValidationError(
                f'Данное поле не должно содержать следующие слова: "казино", "криптовалюта",\
            "крипта", "биржа", "дешево", "бесплатно", "обман", "полиция", "радар"',
                params={"value": value},
            )


class FormForCreate(forms.ModelForm):
    name = forms.CharField(
        label="Наименование",
        validators=[validate_words],
        widget=forms.TextInput(attrs={"class": "form-control", "style": "width: 400px"}),
    )
    description = forms.CharField(
        label="Описание",
        validators=[validate_words],
        widget=forms.Textarea(attrs={"class": "form-control", "style": "height: 100px"}),
    )
    image = forms.ImageField(
        label="Изображение",
        validators=[FileExtensionValidator(["jpeg", "png"], "Изображение может быть формата: 'jpeg', 'png'")],
        widget=forms.FileInput(attrs={"class": "form-control"}),
    )
    category = forms.ModelChoiceField(
        label="Категория",
        queryset=Category.objects.all(),
        widget=forms.Select(attrs={"class": "form-select", "style": "width: 200px"}),
    )
    price = forms.DecimalField(
        label="Цена", widget=forms.TextInput(attrs={"class": "form-control", "style": "width: 200px"})
    )

    def clean_price(self):
        """Валидация цены товара"""
        price = self.cleaned_data.get("price")
        if price < 0:
            raise ValidationError("Цена не может быть меньше 0")
        return price

    def clean_image(self):
        """Валидация размера изображения"""
        image = self.cleaned_data.get("image")
        if image.size > 5242880:
            raise ValidationError("Размер изображения не может быть больше 5 mb")
        return image

    class Meta:
        model = Product
        fields = ["name", "description", "image", "category", "price"]
