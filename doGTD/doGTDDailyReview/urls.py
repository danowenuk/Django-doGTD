from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^', views.daily, name='Daily Review Process'),
    ]