from django.db import models
from users.models import User


class Announcement(models.Model):
    title = models.CharField(
        verbose_name='заголовок объявления',
        max_length=300,
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='announcements',
        verbose_name='автор объявления',
    )
    viewers = models.PositiveIntegerField(
        verbose_name='количество просмотров',
        default=0
    )
    position = models.PositiveSmallIntegerField(
        verbose_name='позиция объявления в ленте'
    )

    def __str__(self):
        return self.title
