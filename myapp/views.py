from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.contrib import messages
from .forms import *

# Create your views here.

def register_user(request):
    msg = None
    success = False
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            email = request.POST.get("email")
            formpostdata = form.save(commit=False)
            formpostdata.email = email
            formpostdata.save()
            
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)
            return redirect("/login/")
        else:
            messages.error(request, 'Form is not valid.')
    else:
        form = SignUpForm()
    return render(request, "myapp/register.html", {"form": form, "msg": msg, "success": success})

# Login Form View
def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if not request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                user = authenticate(username = request.POST.get("username"), password = request.POST.get("password"))
                if user is not None:
                    login(request,user)
                    return redirect('home')
                else:
                    messages.error(request, 'Invalid credentials.')
            else:
                messages.error(request, 'Error validating the form.')
        context = {
            'form':form,
            'msg':msg
        }        
        return render(request, 'myapp/login.html', context)
    return redirect("home")  

def home(request):
    if request.user.is_authenticated:
        return render(request, 'myapp/home.html')
    return redirect('login')                      