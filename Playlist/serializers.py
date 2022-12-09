from rest_framework import serializers
from Playlist.models import Artist, Album
from datetime import datetime


class ArtistSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    created_at = serializers.DateTimeField(auto_now_add=True)
    
    
    def create(self, validated_data):
        return Artist.objects.create(**validated_data)
    
    
    def updated(self, instance, validated_data):    
        instance.name = validated_data.get('title', instance.name)
        instance.created_at = validated_data.get('created', instance.created_at)
        instance.save()
        return instance
        
        
class AlbumSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100,)
    release_date = serializers.DateTimeField(auto_now_add=True, default=datetime.datetime.now)