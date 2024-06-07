from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings



def home(request):
    return render(request,"home.html")


def signup(request):
    if request.method=="POST":
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        my_clients=User.objects.create_user(username,email,password)
        my_clients.save()
        return redirect('http://127.0.0.1:8000/login/')
    return render(request,"signup.html")


def user_login(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('http://127.0.0.1:8000/purchase/')
        else:
            
            return redirect('http://127.0.0.1:8000/signup/')

    return render(request,"login.html")



def pcbuilderpage(request):
    return render(request,"finalhtml.html")

def bloghome(request):
    return render(request,"blog_home.html")

def guide1(request):
    return render(request,"guide1.html")

def guide2(request):
    return render(request,"guide2.html")

def guide3(request):
    return render(request,"guide3.html")

def prebuilt1(request):
    return render(request,"prebuilt1.html")

def prebuilt2(request):
    return render(request,"prebuilt2.html")

def prebuilt3(request):
    return render(request,"prebuilt3.html")





def purchase(request):
    return render(request,"purchase.html")





def newpassword(request):
    return render(request,"newpassword.html")

def OTP(request):
    return render(request,"OTP.html")

def reset(request):
    return render(request,"reset.html")













