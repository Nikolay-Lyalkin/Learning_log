from django.http import HttpResponse, HttpResponseForbidden
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.base import TemplateView, View
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .forms import FormForCreate, FormUpdateProfile
from .models import Category, Contact, Product
from auth_users.models import CustomUser


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = "catalog/product.html"
    context_object_name = "product"
    success_url = reverse_lazy("catalog:home_views")


class UnpublishedProductView(LoginRequiredMixin, PermissionRequiredMixin, View):

    permission_required = 'catalog.can_unpublished_product'
    def post(self, request, pk):
        product = get_object_or_404(Product, id=pk)

        product.is_active = False
        product.save()

        return redirect("catalog:home_views")


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = FormForCreate
    template_name = "catalog/form_add_product.html"
    success_url = reverse_lazy("catalog:home_views")

    def form_valid(self, form):
        form.instance.user = self.request.user

        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = FormForCreate
    template_name = "catalog/form_update_product.html"

    def get_success_url(self):
        return reverse_lazy("catalog:product_views", args=[self.kwargs.get("pk")])


class ProductDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Product
    template_name = "catalog/delete_product.html"
    success_url = reverse_lazy("catalog:home_views")
    permission_required = 'catalog.delete_product'


class ProductListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = "catalog/home.html"
    context_object_name = "products"
    paginate_by = 3

    def get_queryset(self):
        # Получаем только активные объекты
        return Product.objects.filter(is_active=True)



class CatalogProductListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = "catalog/catalog.html"
    context_object_name = "products"

    def get_queryset(self):
        # Получаем только активные объекты
        return Product.objects.filter(is_active=True)


class UnauthorizedUserListView(ListView):
    model = Product
    template_name = "catalog/unauthorized_user.html"
    context_object_name = "products"


class ContactTemplateView(LoginRequiredMixin, TemplateView):
    model = Contact
    template_name = "catalog/contact.html"
    context_object_name = "contacts"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["contact"] = Contact.objects.all()[0]
        return context


class CategoryListView(LoginRequiredMixin, ListView):
    model = Category
    template_name = "catalog/category.html"
    context_object_name = "category"


class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = CustomUser
    template_name = "catalog/profile.html"
    context_object_name = "profile"


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    form_class = FormUpdateProfile
    template_name = "catalog/form_update_profile.html"

    def get_success_url(self):
        return reverse_lazy("catalog:profile_views", args=[self.kwargs.get("pk")])


class ProfilePopupTemplateView(TemplateView):
    model = CustomUser
    template_name = "catalog/popup_question.html"
