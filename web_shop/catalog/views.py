from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home_views(request):
    return render(request, "catalog/home.html")


def category_views(request):
    return render(request, "catalog/category.html")


def catalog_views(request):
    return render(request, "catalog/catalog.html")


def contact_views(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        print(name)
        print(email)
        # Здесь мы просто возвращаем простой ответ
        return HttpResponse(f"Спасибо, {name}! Ваше email {email} получен.")
    return render(request, "catalog/contact.html")
