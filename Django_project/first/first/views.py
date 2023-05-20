from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the First index.")

def help(request):
    return HttpResponse("Project Help Page is Here")