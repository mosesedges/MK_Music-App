from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
import datetime


class Artist(models.Model):
    user = models.ForeignKey(User, related_name='artists', required=True, verbose_name=_('Artist'), on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=255, verbose_name=-_('Artist Name'), required=True,)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True, default=datetime.datetime.now)
    
    
    class Meta:
        verbose_name_plural = _('Artists')
        ordering = ['name', 'created_at']
        
    def __str__(self):
        return self.name
        

class Album(models.Model):
    
    GENRE = (
        (0, _('Soul')),
        (1, _('Jazz')),
        (2, _('R&B')),
        (3, _('Gosple')),
        (4, _('Hip-pop')),
        (5, _('Rap')),
    )
    
    artist = models.ManyToManyField('Artist', on_delete=models.CASCADE)
    title = models.CharField(max_length=225, verbose_name=_('Title'))
    release_date = models.DateField()
    track_no = models.IntegerField(verbose_name=_('Track No'), default=0)
    genre = models.IntegerField(choices=GENRE, verbose_name=_('Genre'), default=0)
    image = models.ImageField(default=None, blank=True)
    
    class Meta:
        verbose_name_plural = _('Artists')
    
    def __str__(self):
        return self.title
    