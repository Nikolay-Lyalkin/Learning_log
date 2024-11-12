from django import forms

from .models import Post


class FormForCreate(forms.ModelForm):
    header = forms.CharField(
        label="Наименование", widget=forms.TextInput(attrs={"class": "form-control", "style": "width: 400px"})
    )
    content = forms.CharField(
        label="Описание", widget=forms.Textarea(attrs={"class": "form-control", "style": "height: 100px"})
    )
    image = forms.ImageField(label="Изображение", widget=forms.FileInput(attrs={"class": "form-control"}))

    is_active = forms.BooleanField(label="Активность публикации", required=False)

    class Meta:
        model = Post
        fields = ["header", "content", "image", "is_active"]
