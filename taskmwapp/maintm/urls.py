from django.urls import path
from . import views

urlpatterns = [
    # path("<int: id>", views.index), to set a variable in path
    path("", views.index),
    path("home/", views.index),
]