from rest_framework import serializers
from .models import User
from announcements.models import Announcement
from djoser.serializers import UserSerializer


class CustomUserSerializer(UserSerializer):
    """ Сериалайзер для djoser'а """
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'user_url')


class AnnouncementsSerializer(serializers.ModelSerializer):
    """ Сериалайзер для отображения списка объявлений у автора """
    class Meta:
        model = Announcement
        fields = ('id', 'title')


class AuthorSerializer(serializers.ModelSerializer):
    """ Сериалайзер для отображения авторов/пользователей """
    announcements = AnnouncementsSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'user_url', 'announcements')
