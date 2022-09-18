from django.shortcuts import render
from django.http import HttpResponse
#from .models import ToDoList, Task
# Create your views here.


def index(response): # add variable name into the function
	#ls = ToDoList.objects.get(id=id) or task_list_name =
	#task = ls.item_set.get(id=task ID number)
	# return HttpResponse("<h1>Django Task Manager %s</h1><br>%s</br>" %(ls.task_list_name, str((item.task))
	return HttpResponse("<h1>Django Task Manager</h1>")    # add %s inside %id outside <> #ls.task_list_name


def home(response):
	return HttpResponse("<h1>Django Home Page!</h1>")
