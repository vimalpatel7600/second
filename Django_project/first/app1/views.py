from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. app1 index page")

def help(request):
    return HttpResponse("app1 help page is here")

def services(request):
    return HttpResponse("app1 services page is here")

def about(request):
    return HttpResponse("app1 about page is here")

def contact(request):
    return HttpResponse("app1 about page is here")
