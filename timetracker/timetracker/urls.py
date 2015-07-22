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
from django.template import Template,Context
from django.views.decorators.csrf import csrf_exempt

raw_template = """<html><body>
                    <p>Hello {{url_name}}.</p>
                    {% ifequal req_mode 'GET' %}
                      <form action="" method="POST">
                        <p>Name: <input type="text" name="rname" rname="" size="10"></p>
                        <p><input type="Submit" value="Submit"></p>
                      </form>
                    {% else %}
                      <p> login name: {{postname}}.</p>
                    {% endifequal %}
                  </body> </html>"""

def hello_world(request):
    return HttpResponse('Hello World')

@csrf_exempt
def hello_any(request,u_name):
    t = Template(raw_template)
    if request.method == 'GET':
        #print(u_name)
        c    = Context({'url_name':u_name,
                        'req_mode':request.method})
        thtml=t.render(c)
        #print(thtml.__str__)
    elif request.method == 'POST':
        postName = request.POST.get('rname')
        #print(postName)
        c    = Context({'url_name':u_name,
                        'req_mode':request.method,
                        'postname':postName})
        thtml=t.render(c)
        #thtml='got it'
        
    return HttpResponse(thtml)
                       
urlpatterns = [
    url(r'^$', hello_world),
    url(r'([^/]+)',hello_any),
    url(r'^admin/', include(admin.site.urls)),
]
