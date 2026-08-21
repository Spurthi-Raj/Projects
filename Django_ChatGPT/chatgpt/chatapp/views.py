import django
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from .forms import UserForm
from django.contrib.auth import authenticate,login,logout
# Create your views here.

def index(request):
    context = {}
    return render(request,'index.html',context)


def signup(request):
    if request.user.is_authenticated:
        return redirect("index")
    form =  UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST['username']
            password = request.POST['password1']
            user = authenticate(request,username = username,password = password)
            if user is not None:
                login(request,user)
                return redirect("index")
    context = {"form":form}

    return render(request,'signup.html',context=context)


def signin(request):
    err = None
    if request.user.is_authenticated:
        return redirect("index")
    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password1']
        user = authenticate(request,username = username,password = password)
        if user is not None:
            login(request,user)
            return redirect("index")
        else:
            err = "Invalid Credentials"
    

    context = {"error":err}
    return render(request,'signin.html',context)


def signout(request):
    logout(request)
    return redirect("signin")