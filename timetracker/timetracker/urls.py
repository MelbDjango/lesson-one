"""timetracker URL Configuration

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
from timetracker import views

def hello_world(request):
    return HttpResponse('Hello ' + request.GET.get("name", "World"))

def hello_debug(request):
    values = request.META.items()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k,v))
    return HttpResponse("<table>%s</table>" % '\n'.join(html))

urlpatterns = [
    url(r'^$', hello_world),
    url(r'^debug/', hello_debug),
    url(r'^name-form/', views.name_form),
    url(r'^sayhello/', views.hello),
    url(r'^admin/', include(admin.site.urls)),
]
