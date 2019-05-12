"""
Serializer module for REST API.
"""

# Django
from rest_framework import serializers

# uploadapp
from .models import Image

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = "__all__"
