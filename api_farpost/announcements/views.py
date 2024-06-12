from rest_framework import generics

from .models import Announcement
from .serializers import AnnouncementsSerializer
from .permissions import IsAuthorOrAdminOrReadOnly


class AnnouncementList(generics.ListCreateAPIView):
    """ Generic класс для модели объявлений, который может вернуть коллекцию или
    создать новую запись в БД """
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementsSerializer

    def perform_create(self, serializer):
        # в автора автоматически записываем юзера
        serializer.save(author=self.request.user)


class AnnouncementDetail(generics.RetrieveUpdateDestroyAPIView):
    """ Generic класс для модели объявлений, который может возвращать,
     обновлять или удалять объекты модели по одному """
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementsSerializer
    # Разрешение на изменение объявления имеет только автор или админ
    permission_classes = (IsAuthorOrAdminOrReadOnly, )
