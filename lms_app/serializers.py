from rest_framework import serializers
from .models import author

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = author
        fields = '__all__'