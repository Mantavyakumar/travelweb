from django.shortcuts import render,HttpResponse,redirect

# Create your views here.
def index(request):
    return render(request, "index.html")

def login(request):
    return render(request, "login.html")
def about(request):
    return render(request, "about.html")
def contact(request):
    return render(request, "contact.html")
def locations(request):
    return render(request, "locations.html")
def register(request):
    return render(request, "register.html")

 