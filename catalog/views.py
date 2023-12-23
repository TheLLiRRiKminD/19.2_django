from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from catalog.models import Product


def contacts(request):
    if request.method == "POST":
        phone = request.POST.get("phone")
        name = request.POST.get("name")
        message = request.POST.get("message")
        print(f"{name} ({phone}): {message}")
    return render(request, 'catalog/contacts.html')


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/product_list.html'


class ProductDetailView(DetailView):
    model = Product


class ProductCreateView(CreateView):
    model = Product
    fields = ('name', 'description', 'image',)
    success_url = reverse_lazy('catalog:list')


class ProductUpdateView(UpdateView):
    model = Product
    fields = ('name', 'description', 'image',)


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:home')
