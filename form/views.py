from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse
import json
from form.models import Form
from requests import get

"""
from .serializers import FormSerializer
"""

# Create your views here.
def AddForm(request):
    return render(request, "home.html")

def home_view(request):
    data = request.POST["username"]
    print(data)
    return render(request, "home.html")

def registration(request):
    ip = get('https://api.ipify.org').text
    print("THE IP: "+ip)
    return render(request, "reg/index.html")

def RegistrationAction(request):
    ip = get('https://api.ipify.org').text
    email = request.POST.get('email', False);
    username = request.POST.get('username', False);
    password = request.POST.get('password', False);
    print(ip, email, username, password)
    return render(request, "reg/index.html")

"""
def home_view(request):

    # logic of view will be implemented here
    print(request.POST)
    data = {
        'name': request.POST["your_name"],
    }
    serializer = FormSerializer(data=data)
    if serializer.is_valid():
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return render(request, "home.html")
"""
