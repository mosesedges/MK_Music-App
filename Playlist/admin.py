from django.contrib import admin

from .  import models

@admin.register(models.Artist)

class ArtAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'created_at',
    ]
    
@admin.register(models.Album)

class AlbAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'genre',
    ]
