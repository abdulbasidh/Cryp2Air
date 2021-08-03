from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse
import json
from form.models import Form
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
    return render(request, "reg/index.html")

def RegistrationAction(request):
    email = request.POST.get('email', False);
    password = request.POST.get('password', False);
    print(email, password)
    red = redirect('/registration/')
    return red
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
