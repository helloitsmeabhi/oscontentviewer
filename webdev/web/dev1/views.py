from django.shortcuts import render, redirect
from django.http import *
from .forms import *
from .models import *
from django.contrib.auth import authenticate, login
from django.contrib import messages
def signup(request):
    if request.method == 'POST':
        username = request.POST['Name']
        password = request.POST['Password']
        
        try:
            u=User(name=username,password=password)
            u.save()
            return redirect('mainpage')  # Redirect to domains page

        except User.DoesNotExist:
            messages.error(request, 'Invalid credentials')

    return render(request, "signup.html")

def mainpage(request):
    return render(request, "mainpage.html")
def index(request):
    return render(request,"index.html")

def domain(request):
    return render(request,"domains.html")
def eng(request):
    return render(request,"engineering.html")
def  trig(request):
    return render(request,"trigonometry.html")
def cal(request):
    return render(request,"calculus.html")
def angu(request):
    return render(request,"angularmomentum.html")
def math(request):
    return render(request,"maths.html")
def science(request):
    return render(request,"science.html")
def per(request):
    return render(request,"periodic.html")
def hindi(request):
    return render(request,"hindi.html")
def english(request):
    return render(request,"english.html")

def lang(request):
    return render(request,"languages.html")
def gemini(request):
    return render(request,"gemini.html")

def kan(request):
    return render(request,"kannada.html")

def login(request):
    if request.method == 'POST':
        username = request.POST['Name']
        password = request.POST['Password']
        
        try:
            user = User.objects.get(name=username)
            if user.password == password:
                # Login the user
                # You can also use Django's built-in authentication system here
                return redirect('domain')  # Redirect to domains page
            else:
                messages.error(request, 'Invalid credentials')
        except User.DoesNotExist:
            messages.error(request, 'Invalid credentials')

    return render(request, 'login.html')

def search(request):
    return render(request,"search.html")


def arith(request):
    return render(request,"arithmetic.html")

def alg(request):
    return render(request,"algebra.html")

def elec(request):
    return render(request,"electrostatic.html")

def bio(request):
    return render(request,"biology.html")
def ml(request):
    return render(request,"machinelearning.html")
def dsa(request):
    return render(request,"dsa.html")