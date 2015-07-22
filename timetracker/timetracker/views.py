from django.shortcuts import render
from django.http import HttpResponse

def name_form(request):
	return render(request, 'name-form.html')

def hello(request):
	if 'name' in request.GET:
		received = request.GET.get("name", "World")
		if len(received) == 0:
			received = "World"
		return render(request, 'hello.html', {'name':received})
