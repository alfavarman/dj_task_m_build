from django.shortcuts import render, redirect
from .forms import RegistrationForm
# Create your views here.


def register(response):
    creation_form = RegistrationForm
    if response.method == "POST":
        form = creation_form(response.POST)
        if form.is_valid():
            form.save()

        return redirect("/home")
    else:
        form = creation_form()

    return render(response, "register/register.html", {"form": form})
