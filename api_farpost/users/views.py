from rest_framework import generics

from .models import User
from .serializers import AuthorSerializer


class AuthorList(generics.ListAPIView):
    """ Generic класс только для отображения коллекции авторов"""
    queryset = User.objects.all()
    serializer_class = AuthorSerializer


class AuthorDetail(generics.RetrieveAPIView):
    """ Generic класс разрешает только чтение информации о конкретном авторе"""
    queryset = User.objects.all()
    serializer_class = AuthorSerializer
