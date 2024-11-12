from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .forms import FormForCreate
from .models import Category, Contact, Product


class ProductDetailView(DetailView):
    model = Product
    template_name = "catalog/product.html"
    context_object_name = "product"
    success_url = reverse_lazy("catalog:home_views")


class ProductCreateView(CreateView):
    model = Product
    form_class = FormForCreate
    template_name = "catalog/form_add_product.html"
    success_url = reverse_lazy("catalog:home_views")

    def form_valid(self, form):
        form.instance.user = self.request.user

        return super().form_valid(form)


class ProductUpdateView(UpdateView):
    model = Product
    form_class = FormForCreate
    template_name = "catalog/form_update_product.html"
    success_url = reverse_lazy("catalog:home_views")


class ProductListView(ListView):
    model = Product
    template_name = "catalog/home.html"
    context_object_name = "products"
    paginate_by = 3


class ContactTemplateView(TemplateView):
    model = Contact
    template_name = "catalog/contact.html"
    context_object_name = "contacts"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["contact"] = Contact.objects.all()[0]
        return context


# Create your views here.
# def home_views(request):
#     if request.method == "POST":
#         name = request.POST.get("name")
#         description = request.POST.get("description")
#         image = request.POST.get("image")
#         categories = Category.objects.all()
#         category = [category for category in categories if request.POST.get("category") == category.name]
#         price = request.POST.get("price")
#
#         new_product = Product.objects.create(
#             name=name, description=description, image=image, category=category[0], price=price
#         )
#
#         # Здесь мы просто возвращаем простой ответ
#         return HttpResponse(f"Вы добавили товар - {name}!")
#
#     categories = Category.objects.all()
#     products = Product.objects.all()
#
#     paginator = Paginator(products, 3)
#     page_number = request.GET.get("page", 1)
#     page_obj = paginator.get_page(page_number)
#
#     context = {
#         "products": products,
#         "categories": categories,
#         "page_obj": page_obj,
#     }
#
#     return render(request, "catalog/home.html", context)


def category_views(request):
    return render(request, "catalog/category.html")


def catalog_views(request):
    return render(request, "catalog/catalog.html")


# def contact_views(request):
#     if request.method == "POST":
#         name = request.POST.get("name")
#         email = request.POST.get("email")
#         print(name)
#         print(email)
#         # Здесь мы просто возвращаем простой ответ
#         return HttpResponse(f"Спасибо, {name}! Ваше email {email} получен.")
#     contacts = Contact.objects.get(id=1)
#     contact = {"phone_number": contacts.phone_number, "address": contacts.address, "email": contacts.email}
#     return render(request, "catalog/contact.html", contact)

# def product_views(request, product_id):
#     product = Product.objects.get(id=product_id)
#     context = {"product": product}
#     return render(request, "catalog/product.html", context)
