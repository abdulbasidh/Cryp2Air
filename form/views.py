from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse
import json
from form.models import Users, Session
from requests import get
from .serializers import UsersSerializer, SessionSerializer
import hashlib
import string
import random

# Create your views here.
"""
def DashboardView(request):
    ses = request.GET['ses']
    try:
        if Session.objects.filter(token=ses).exists():
            if Session.objects.filter(status="active").exists():
                data1 = Session.objects.get(token=ses)
                email = data1.email
                data2 = Users.objects.get(email=email)
                username = data2.username
                context = {
                "ses": ses,
                "email": email,
                "username": username,
                }
                return render(request, "dashboard.html", context)
            else:
                response = redirect('/login/')
                return response
        else:
            response = redirect('/login/')
            return response
    except KeyError:
        response = redirect('/login/')
        return response
    return render(request, "dashboard.html", context)

def logout(request):
    ses = request.GET['ses']
    try:
        if Session.objects.filter(token=ses).filter(status="active").exists():
            Session.objects.filter(token=ses).update(status="inactive")
            response = redirect('/login/')
            response.delete_cookie('ses')
            return response

        else:
            response = redirect('/login/')
            return response
    except KeyError:
        response = redirect('/login/')
        return response
    return render(request, "page-login.html")
"""

def login(request):
    try:
        ses  = request.COOKIES['ses']
        if Session.objects.filter(token=ses).filter(status="active").exists():
            response = redirect('/dashboard/?ses='+ses)
            return response
        else:
            return render(request, "page-login.html")
    except KeyError:
        return render(request, "page-login.html")

def LoginAction(request):
    # Getting credentials
    ip = get('https://api.ipify.org').text
    email = request.POST.get('email', False);
    password = request.POST.get('password', False);

    # Encrypting password
    password_gen = hashlib.sha256(password.encode())
    encryppass=password_gen.hexdigest()
    rawtoken=''.join(random.choices(string.ascii_uppercase + string.digits, k = 7))
    token_gen = hashlib.sha256(rawtoken.encode())
    ses=token_gen.hexdigest()

    if Users.objects.filter(email=email).exists():
        if Users.objects.filter(password=encryppass).exists():
            data = {
                'email': email,
                'token': ses,
                'status': 'active',
                'ip': ip,
            }
            serializer = SessionSerializer(data=data)
            if serializer.is_valid():
                serializer.save()

            response = redirect('/dashboard/?ses='+ses)
            response.set_cookie('ses', ses)
            return response
        else:
            result="email or password does not match"
            response = redirect('/dashboard/?a='+result)
            return response
    else:
        result="email or password does not match"
        response = redirect('/dashboard/?a='+result)
        return response

def registration(request):
    try:
        ses  = request.COOKIES['ses']
        if Session.objects.filter(token=ses).filter(status="active").exists():
            response = redirect('/dashboard/?ses='+ses)
            return response
        else:
            return render(request, "page-register.html")
    except KeyError:
        return render(request, "page-register.html")

def registrationError(request):
    key = request.GET['status']
    context = {
    "status": key,
    }
    return render(request, "page-register.html", context)

def registrationConfirm(request):
    key = request.GET['status']
    context = {
    "status": key,
    }
    return render(request, "page-login.html", context)

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
        response = redirect('/registrationError/?status='+result)
        return response
    elif Users.objects.filter(email=email).exists():
        result="email exists"
        response = redirect('/registrationError/?status='+result)
        return response
    else:
        # Printing to terminal
        print(ip, email, username, encryppass)

        # Saving in DB
        users = Users(email=email,username=username,password=encryppass)
        users.save()

        # Redirecting to dashboard
        """
        response = redirect('/dashboard/?a='+username)
        """
        result="Your account is registered!"
        response = redirect('/registrationConfirm/?status='+result)

        return response
        return render(request, "loginreg/registration.html")

def setcookie(request):
    cook = HttpResponse("")
    test = "test1"
    cook.set_cookie('java-tutorial', 'javatpoint.com')
    return cook
    print(test)

def delcookie(request):
    cook = HttpResponse("Cookie Deleted")
    cook.delete_cookie('ses')
    return cook

def getcookie(request):
    tutorial  = request.COOKIES['ses']
    print(tutorial)
    return HttpResponse("java tutorials @: "+  tutorial);
