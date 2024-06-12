from rest_framework import serializers
from .models import Announcement
from users.models import User


class AuthorSerializer(serializers.ModelSerializer):
    """ Сериалайзер для отображения информации об авторе """
    class Meta:
        model = User
        fields = ('id', 'username')


class AnnouncementsSerializer(serializers.ModelSerializer):
    """ Сериалайзер для объявлений """
    author = AuthorSerializer(read_only=True)

    class Meta:
        model = Announcement
        fields = ('id', 'title', 'author', 'viewers', 'position')
