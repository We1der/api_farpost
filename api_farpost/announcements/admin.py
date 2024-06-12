from django.contrib import admin
from .models import Announcement


class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'viewers', 'position')


admin.site.register(Announcement, AnnouncementAdmin)
