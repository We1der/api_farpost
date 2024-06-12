from django.urls import path

from .views import AuthorList, AuthorDetail

urlpatterns = [
    path('authors/', AuthorList.as_view()),
    path('authors/<int:pk>/', AuthorDetail.as_view()),
]
