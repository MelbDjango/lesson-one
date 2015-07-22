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


def hello_world(request, name):
   name = request.GET.get('name')
   #
   # Start of corner cutting
   #
   ghetto_template = "<html>\n\
                      <head>\n\
                        <title>GaaS - Greeting as a Service</title>\n\
                      </head>\n\
                      <body>\n\
                        <h1>Hello {0}!</h1>\n\
                        <br><br>\n\
                        Enter your name to receive a special prize:\n\
                        <br>\n\
                        <form>\n\
                         <input type='text' name='name'><br>\n\
                         <input type='submit' value='Submit'>\n\
                        </form>\n\
                      </body>\n\
                      </html>"
   #
   # End of corner cutting
   # 
   if name:
      return HttpResponse(ghetto_template.format(name))

   return HttpResponse(ghetto_template.format("world"))

urlpatterns = [
    url(r'^(?P<name>)$', hello_world),
    url(r'^admin/', include(admin.site.urls)),
]
