from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Task
# Create your views here.

#
def index(response, id):
	ls = ToDoList.objects.get(id=id)
	# value = Task.task.
	return render(response, 'maintm/list.html', {"ls": ls})


