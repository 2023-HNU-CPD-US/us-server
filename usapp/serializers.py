from rest_framework import serializers
from .models import Folder, Text

class TextSerializer(serializers.ModelSerializer):
    class Meta:
        model = Text
        fields = ['id', 'name', 'created_at', 'content', 'parentId', 'type']

class FolderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Folder
        fields = ['id', 'name', 'created_at', 'parentId', 'type']