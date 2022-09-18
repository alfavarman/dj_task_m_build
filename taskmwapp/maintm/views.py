from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList, Task
from .forms import CreateNewList
# Create your views here.


def index(response, id):
	ls = ToDoList.objects.get(id=id)
	return render(response, 'maintm/list.html', {"ls": ls})


def home(response):
	return render(response, 'maintm/home.html', {})


def create(response):
	# depending on request to be get or post
	if response.method == "POST":
		form = CreateNewList(response.POST)

		if form.is_valid():
			n = form.cleaned_data["name"]
			t = ToDoList(tasks_list_name=n)
			t.save()
			return HttpResponseRedirect("/%i" %t.id)
	else:
		form = CreateNewList()

	return render(response, 'maintm/create.html', {"form": form})


def about(response):
	return render(response, 'maintm/about.html', {})
