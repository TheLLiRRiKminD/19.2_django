from django.shortcuts import render

from catalog.models import Product


# Create your views here.

def home(request):
    product_list = Product.objects.all()
    context ={
        'object_list': product_list
    }
    return render(request, 'catalog/home.html', context)


def contacts(request):
    if request.method == "POST":
        email = request.POST.get("email")
        name = request.POST.get("name")
        message = request.POST.get("message")
        print(f"{name} ({email}): {message}")
    return render(request, 'catalog/contacts.html')
