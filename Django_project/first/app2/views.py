from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("app2 index page is here")

def about(request):
    return HttpResponse("app2 about page is here")

def services(request):
    return HttpResponse("app2 services page is here")

def help(request):
    return HttpResponse("app2 help page is here")

def contact(request):
    return HttpResponse("app2 contact page is here")
