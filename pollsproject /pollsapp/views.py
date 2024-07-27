# from django.shortcuts import render
from django.http import HttpResponse

def poll(request):
    return HttpResponse ("hello, Welcome to the polling application")

