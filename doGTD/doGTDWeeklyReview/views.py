from django.shortcuts import render
from django.http import HttpResponse

def simple(request):
    return HttpResponse("<h2>Simple HTML page...</h2>")

def weekly(request):
    return render(request, 'doGTDCollect/basic.html',{'content':['Simple placeholder for Daily review process...']})
