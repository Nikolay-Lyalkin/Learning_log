from auth_users.models import CustomUser
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import Permission
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.base import TemplateView, View
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .forms import FormForCreate, FormUpdateProfile
from .models import Category, Contact, Product


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = "catalog/product.html"
    context_object_name = "product"
    success_url = reverse_lazy("catalog:home_views")


class UnpublishedProductView(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = "catalog.can_unpublished_product"

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
        user = self.request.user
        product = form.save()
        product.owner = user
        product.save()

        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = FormForCreate
    template_name = "catalog/form_update_product.html"

    def get_success_url(self):
        return reverse_lazy("catalog:product_views", args=[self.kwargs.get("pk")])

    def get_object(self, queryset=None):
        product = super().get_object(queryset)
        user = self.request.user

        if product.owner != user:
            raise PermissionDenied("Вы не можете редактировать этот продукт.")

        return product


class ProductDeleteView(LoginRequiredMixin, PermissionDenied, DeleteView):
    model = Product
    template_name = "catalog/delete_product.html"
    success_url = reverse_lazy("catalog:home_views")

    def get_object(self, queryset=None):
        product = super().get_object(queryset)
        user = self.request.user

        if product.owner != user and not user.has_perm("catalog.delete_product"):
            raise PermissionDenied("Вы не можете удалять этот продукт.")

        return product


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


def custom_permission_denied(request, exception):
    return render(request, "catalog/403.html", {"message": str(exception)})
