from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Welcome to home page")

def about(request):
    return HttpResponse("Welcome to about page")

def contact(request):
    return HttpResponse("Welcome to contact page")