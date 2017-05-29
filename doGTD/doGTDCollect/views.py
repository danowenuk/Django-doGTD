from django.shortcuts import render
from django.http import HttpResponse

def index2(request):
    return HttpResponse("<h2>doGTD Collect App placeholder</h2>")

def index(request):
    return render(request, 'doGTDCollect/home.html')