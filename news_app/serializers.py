from rest_framework import serializers
from django.contrib.auth.models import User
from .models import News

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=6)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'password']

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user


class NewsSerializer(serializers.ModelSerializer):
    author_name = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = News
        fields = [
            'id',
            'title',
            'summary',
            'content',
            'author',
            'author_name',
            'media_file',
            'date_created',
            'date_updated',
        ]
        read_only_fields = ['author', 'date_created', 'date_updated']

    def validate_content(self, value):
        if len(value) < 50:
            raise serializers.ValidationError('Минимум 50 символов.')
        return value