from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(response):
	return HttpResponse("<h1>Django Task Manager</h1>")


def home(response):
	return HttpResponse("<h1>Django Home Page!</h1>")
