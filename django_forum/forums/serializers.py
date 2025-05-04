from rest_framework import serializers
from .models import Category, Forum, Message, Ad

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'content', 'created_at', 'image', 'created_at']

class ForumSerializer(serializers.ModelSerializer):
    messages = MessageSerializer(many=True, read_only=True)

    class Meta:
        model = Forum
        fields = ['id', 'name', 'description', 'messages', 'image', 'created_at']

class CategorySerializer(serializers.ModelSerializer):
    forums = ForumSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'forums']

class AdsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = ['id', 'image', 'link']