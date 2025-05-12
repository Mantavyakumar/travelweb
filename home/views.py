from django.shortcuts import render,HttpResponse,redirect
from home.models import Contact   
from .forms import ContactForm,  Registration
from .models import Contact as ContactModel 
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import RegistrationForm
from .models import  Registration
  
# Create your views here.
def index(request):
    return render(request, "index.html")

def loginuser(request):
 
    if request.method =="POST":
        username =request.POST.get('username')
        password =request.POST.get('password')
        user = authenticate(username=username, password=password)
     
        if user is not None:
         print(username,password)
         login(request,user)
         messages.success(request, f'Hey {username}, welcome to GO QUEST!')
         return redirect("/index/")
         
        else:
         return render(request, "login.html")
    
    return render(request, "login.html")

def logoutuser(request):
    logout(request)
    
    return redirect("/")
def about(request):
    return render(request, "about.html")
def itenary(request):
    return render(request,"itenary.html")
 
def locations(request):
    return render(request, "locations.html")

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
           form.save()
            
        return redirect('index.html')
    else:
        form = RegistrationForm()

    return render(request, 'register.html', {'form': form})

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'contact1.html', {'form': ContactForm(), 'success': True})
    else:
        form = ContactForm()
    
    return render(request, 'contact1.html', {'form': form})
def reg(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists. Try another.')
        else:
            # Create user
            user = User.objects.create_user(username=username, password=password)
            user.save()

            # Authenticate and login
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                 
                messages.success(request, f'Welcome, {username}! You are now logged in.')
                return redirect('/index/')  # Change this to your desired landing page
               
            else:
                messages.error(request, 'Something went wrong with login. Try manually.')

    return render(request, 'reg.html')




def medical(request):
    
    return render(request, 'medical.html')

 