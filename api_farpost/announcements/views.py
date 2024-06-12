from rest_framework import generics

from .models import Announcement
from .serializers import AnnouncementsSerializer


class AnnouncementList(generics.ListCreateAPIView):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementsSerializer


class AnnouncementDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementsSerializer
