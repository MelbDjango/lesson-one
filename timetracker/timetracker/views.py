from django.shortcuts import render
from django.http import HttpResponse

def name_form(request):
	return render(request, 'name-form.html')

def hello(request):
	if 'name' in request.GET:
		return HttpResponse("Hello " + request.GET['name'])
