from rest_framework import serializers
from django.contrib.auth.models import User
from form.models import Users

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ["email","username","password"]
