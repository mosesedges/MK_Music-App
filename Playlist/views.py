from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    return HttpResponse('Playlist Application')


def age(request, age):
    return HttpResponse('my new age is %s' % age)