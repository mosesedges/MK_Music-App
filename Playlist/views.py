from django.shortcuts import render
from django.http import HttpResponse
from .models import *


# Create your views here.


def home(request):
    return HttpResponse('Playlist Application')


def age(request, age):
    return HttpResponse('my new age is %s' % age)