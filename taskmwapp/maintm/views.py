from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Task
# Create your views here.


def index(response, id):
	ls = ToDoList.objects.get(id=id)
	# value = Task.task.
	return render(response, 'maintm/list.html', {"ls": ls})


def home(response):
	return render(response, 'maintm/home.html', {})


def create(response):
	return render(response, 'maintm/create.html', {})


def about(response):
	return render(response, 'maintm/about.html', {})
