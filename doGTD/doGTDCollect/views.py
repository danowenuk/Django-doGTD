from django.shortcuts import render
from django.http import HttpResponse

def simple(request):
    return HttpResponse("<h2>A simple HTML page...</h2>")

def index(request):
    return render(request, 'doGTDCollect/home.html')

def workflow(request):
    return render(request, 'doGTDCollect/workflow.html')

def contact(request):
    return render(request, 'doGTDCollect/basic.html',{'content':['If you would like to contact me, please email me.','danowen@gmail.com']})