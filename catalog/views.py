from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request, 'catalog/home.html')


def contacts(request):
    if request.method == "POST":
        email = request.POST.get("email")
        name = request.POST.get("name")
        message = request.POST.get("message")
        print(f"{name} ({email}): {message}")
    return render(request, 'catalog/contacts.html')
