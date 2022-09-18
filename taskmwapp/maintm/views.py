from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList, Task
from .forms import CreateNewList
# Create your views here.


def index(response, id):
	ls = ToDoList.objects.get(id=id)

	# {"save": ["save"], "c1": ["ticked"]}
	if response.method == "POST":
		print(response.POST)
		if response.POST.get("save"):
			for position in ls.task_set.all():
				if response.POST.get("c" + str(position.id)) == "ticked":
					position.completed = True
				else:
					position.completed = False
				position.save()

		elif response.POST.get("newItem"):
			txt = response.POST.get("new")

			# as we dont use django forms here manual validation is required
			# TODO implement validator
			if len(txt) > 3:
				ls.task_set.create(task=txt, completed=False)
			else:
				print("task text must be at last 4 characters long")
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
