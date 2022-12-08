from django.shortcuts import render
from django.shortcuts import HttpResponse

def hola(request):
	return HttpResponse("hola, Mundo ")

def vader(request):
	return HttpResponse("hola,  Vader")
	



