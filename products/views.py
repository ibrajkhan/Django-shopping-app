from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("hello world !")


def new_page(request):
    return HttpResponse('New products')

