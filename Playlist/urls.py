from Playlist import views
from django.urls import path


urlpatterns = [
    path('', views.home, name='playlist'),
]
