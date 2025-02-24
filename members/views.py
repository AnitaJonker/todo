from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


# register new user
def registerPage(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login_user")
        else:
            messages.error(request, ("There was an error registering, try again."))
    context = {"form": form}
    return render(request, "authenticate/register.html", context)


# login user and show index if successful login
def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome back: {username}")
            print("logged in")
            return redirect("index")
        else:
            messages.error(request, ("There was an error logging in, try again."))
            return redirect("login_user")

    else:
        return render(request, "authenticate/login.html")


# logout user and show logout screen
def logout_view(request):
    logout(request)
    return render(request, "authenticate/logged_out.html")
