"""kittens URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.http import HttpResponse
import random

def hello (request):

    name=request.GET.get("name","default")
    return HttpResponse('<b>hello</b> '+name)

def displayform (request):
    return HttpResponse("""<form action="hello">
First name:<br>
<input type="text" name="name" value="Noob">
<br>
<input type="submit" value="Submit">
</form> """)
urlpatterns = [
    url(r'^$', displayform),
    url(r'^hello$', hello),
    url(r'^admin/', include(admin.site.urls)),
]
