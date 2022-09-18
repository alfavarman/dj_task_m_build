from django.db import models

# Create your models here.


class ToDoList(models.Model):
    tasks_list_name = models.CharField(max_length=150)
    objects = models.Manager()

    def __str__(self):
        return self.tasks_list_name


class Task(models.Model):
    # on_delete=CASCADE if native key deleted forign follow
    todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    task = models.CharField(max_length=300)
    completed = models.BooleanField()
    objects = models.Manager()

    def __str__(self):
        return self.task

