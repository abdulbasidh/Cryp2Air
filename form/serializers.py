from rest_framework import serializers
from django.contrib.auth.models import User
from form.models import Form

class FormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Form
        fields = ["username"]
