from django.shortcuts import render
from django.http import HttpResponse

def dashboard(request):
    return HttpResponse("<h2>Placeholder for GTD Dashboard...</h2>")
