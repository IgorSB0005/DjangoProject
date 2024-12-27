from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout


# Create your views here.
def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            login(request, form.save())
            return redirect("posts:list")
        else:
            messages.error(request, "All conditions are not met, check username or password")
    else:
        form = UserCreationForm()
    return render(request, "users/register.html", {"form" : form})


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect("posts:list")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
        storage = messages.get_messages(request)
        storage.used = True
    return render(request, "users/login.html", {"form" : form})


def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("posts:list")