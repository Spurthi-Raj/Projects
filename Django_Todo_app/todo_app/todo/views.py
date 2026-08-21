from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from todo import models
from todo.models import ToDo
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required 

# Create your views here.

def signup(request):
    if request.method == 'POST':
        fnm = request.POST.get('fnm')
        email = request.POST.get('email')
        pwd = request.POST.get('pwd')
        my_user = User.objects.create_user(fnm,email,pwd)
        my_user.save()
        return redirect("/login")
    return render(request,'signup.html')

def login_form(request):
    if request.method == 'POST':
        fnm=request.POST.get('fnm')
        pwd=request.POST.get('pwd')
        print(fnm,pwd)
        userr=authenticate(request,username=fnm,password=pwd)
        if userr is not None:
            login(request,userr)
            return redirect('/todo')
        else:
            return redirect('/login')
               

    return render(request,"login.html")

@login_required(login_url='login_form')
def todo(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        obj = models.ToDo(title=title,user=request.user)
        obj.save()
        user=request.user 
        res = models.ToDo.objects.filter(user = user).order_by('-date')
        return redirect('/todo',{'res':res})
    res = models.ToDo.objects.filter(user = request.user).order_by('-date')
    return render(request,"todo.html",{'res':res,})


@login_required(login_url='login_form')
def edit_todo(request,srno):
    if request.method == 'POST':
        title = request.POST.get('title')
        obj = models.ToDo.objects.get(srno=srno)
        obj.title = title
        obj.save()
        return redirect('/todo')
    obj = models.ToDo.objects.get(srno=srno)
    return render(request,"edit_todo.html",{'obj':obj})


def delete_todo(request,srno):
    obj = models.ToDo.objects.get(srno=srno)
    obj.delete()
    return redirect('/todo')