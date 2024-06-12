from rest_framework import serializers
from .models import Announcement


class AnnouncementsSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Announcement
        fields = ('id', 'title', 'author', 'viewers', 'position')
