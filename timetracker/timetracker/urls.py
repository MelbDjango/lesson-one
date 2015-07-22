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


def hello_world(request):
	name = request.GET.get("name", None)
	if name:
		res = "Welcome %r" % name
	else:
		res = 'No name... please enter one'
	http_res = '<html><body>'
	http_res += '<b>' + res + '</b>'
	http_res += '<form method="get">'
	http_res += '<input type="text" name="name">'
	http_res += '<input type="submit" value="Submit"/>'
	http_res += '</form></body></html>'
	
		
	return HttpResponse(http_res)


urlpatterns = [
    url(r'^$', hello_world),
    url(r'^admin/', include(admin.site.urls)),
]
