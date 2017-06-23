from django.conf.urls import url
from django.views.generic import ListView, DetailView
from doGTDProcess.models import Action
from . import views
from django.db.models.query import QuerySet

urlpatterns = [
        url(r'^$', ListView.as_view(
                                    queryset = Action.objects.all().order_by("-date")[:25],
                                    template_name = "doGTDProcess/action_list.html")),
        url(r'^(?P<pk>\d+)$', DetailView.as_view(model = Action,
                                                 template_name = 'doGTDProcess/action_detail.html')),
               
               
        url(r'^new/$', views.action_new, name='action_new'), 
        url(r'^(?P<pk>\d+)/edit/$', views.action_edit, name='action_edit'),
        
        url(r'^dashboard', views.dashboard, name='doGTD Dashboard'),
    ]