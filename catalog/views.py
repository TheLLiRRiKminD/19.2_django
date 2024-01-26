from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.cache import cache
from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import ProductForm, VersionForm
from catalog.models import Product, Version
from .utils import get_category_subjects


@login_required
def contacts(request):
    if request.method == "POST":
        phone = request.POST.get("phone")
        name = request.POST.get("name")
        message = request.POST.get("message")
        print(f"{name} ({phone}): {message}")
    return render(request, 'catalog/contacts.html')


class ProductListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'catalog/product_list.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['category_list'] = get_category_subjects(self.object_list)
        return context_data


class ProductDetailView(LoginRequiredMixin, DetailView):
    permission_required = 'catalog.view_product'
    model = Product

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        if settings.CACHE_ENABLE:
            key = f"category_product_{self.object.pk}"
            category_product = cache.get(key)
            if category_product is None:
                category_product = self.object.category_id
                cache.set(key, category_product)
        else:
            category_product = self.object.category_id
        context_data['category_product'] = category_product
        return context_data


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    permission_required = 'catalog.create_product'
    success_url = reverse_lazy('catalog:list')

    def form_valid(self, form):
        current_user = self.request.user
        obj = form.save(commit=False)
        obj.created_by = current_user
        obj.save()
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    permission_required = 'catalog.change_product'
    success_url = reverse_lazy('catalog:list')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == "POST":
            context_data['formset'] = VersionFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = VersionFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:list')
