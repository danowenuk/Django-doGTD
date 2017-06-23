from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse
from .forms import ActionForm
from .models import Action
import time

def simple(request):
    return HttpResponse("<h2>Simple HTML page</h2>")

def dashboard(request):
    return render(request, 'doGTDCollect/basic.html',{'content':['Simple placeholder for Dashboard page']})

def action_new(request):
    if request.method == "POST":
        form = ActionForm(request.POST)
        if form.is_valid():
            action = form.save(commit=False)
            action.save()
            return redirect('/process')
    else:
        form = ActionForm(initial={'date':time.strftime("%Y-%m-%d %H:%M:%S"),
                                   'title':'Testing action @ ' + time.strftime("%H:%M:%S"),
                                   'description': 'some default initial value'
                                   ,'context':'phone'})
    return render(request, 'doGTDProcess/action_edit.html', {'form': form})

def action_edit(request, pk):
    action = get_object_or_404(Action, pk=pk)
    if request.method == "POST":
        form = ActionForm(request.POST, instance=action)
        if form.is_valid():
            action = form.save(commit=False)
            action.save()
            return redirect('/process/' + pk)
    else:
        form = ActionForm(instance=action)
    return render(request, 'doGTDProcess/action_edit.html', {'form': form})