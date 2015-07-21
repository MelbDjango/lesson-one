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
from django.views.decorators.http import require_http_methods

# If there's no name, display a form asking for name.
# This is the HTML for that form.
form_page_html = """
  <html>
    <body>
      <p>Hi, what's your name?</p>

      <form method="GET">
        <input type="text" name="name" />
      </form>
    </body>
  <html>
"""

@require_http_methods(('GET',))
def hello_world(request):
    """
    A view which asks for someone's name if there's no 'name'
    in the request.GET dict, or says hello to 'name' if there is.
    Only the GET method is supported.
    """

    # By checking for 'name' in the GET dict of the request
    if 'name' in request.GET:
        response_str = 'Hello {}'.format(request.GET['name'])
    else:
        response_str = form_page_html

    """
    # By fishing out 'name' from the GET dict of the request,
    # and if it's missing, catch the exception and default to
    # the form.
    try:
        response_str = 'Hello {}'.format(request.GET['name'])
    except KeyError:
        response_str = form_page_html
    """

    return HttpResponse(response_str)

urlpatterns = [
    url(r'^$', hello_world),
    url(r'^admin/', include(admin.site.urls)),
]
