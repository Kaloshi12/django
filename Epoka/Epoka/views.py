from django.shortcuts import render
from django.http import HttpResponse


def hello_World(request):
    return HttpResponse("Hello World")
