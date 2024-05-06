from rest_framework import serializers
from .models import Art

class PageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Art 
        fields = ('name', 'preview', 'likes', 'description')