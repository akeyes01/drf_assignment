from rest_framework import serializers
from .models import Author

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        #fields = '__all__'
        fields = ['author_id', 'author', 'owner']
        read_only_fields = ['owner']

    def create(self, validated_data):
        return Author.objects.create(**validated_data)