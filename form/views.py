from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse
import json
from form.models import Users
from requests import get
from .serializers import UsersSerializer
import hashlib


# Create your views here.
def AddForm(request):
    return render(request, "home.html")

def DashboardView(request):
    key = request.GET['a']
    context = {
    "name": key,
    }
    return render(request, "dashboard.html", context)

def home_view(request):
    data = request.POST["username"]
    print(data)
    return render(request, "home.html")

def registration(request):
    ip = get('https://api.ipify.org').text
    print("THE IP: "+ip)
    return render(request, "reg/index.html")

def RegistrationAction(request):

    # Getting credentials
    ip = get('https://api.ipify.org').text
    email = request.POST.get('email', False);
    username = request.POST.get('username', False);
    password = request.POST.get('password', False);

    # Encrypting password
    password_gen = hashlib.sha256(password.encode())
    encryppass=password_gen.hexdigest()

    if Users.objects.filter(username=username).exists():
        result="username exists"
        response = redirect('/dashboard/?a='+result)
        return response
    elif Users.objects.filter(email=email).exists():
        result="email exists"
        response = redirect('/dashboard/?a='+result)
        return response
    else:
        # Printing to terminal
        print(ip, email, username, encryppass)

        # Saving in DB
        users = Users(email=email,username=username,password=encryppass)
        users.save()

        # Redirecting to dashboard
        response = redirect('/dashboard/?a='+username)

        return response
        return render(request, "reg/index.html")
