from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# Create your views here.


def landing(request):
    return render(request, "todo/landing.html")


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # redirect to the home page after login
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def logout(request):
    return render(request, "todo/logout.html")  


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after signup
            return redirect("home")  # Redirect to homepage after signup
    else:
        form = UserCreationForm()
    return render(request, "registration/signup.html", {"form": form})


def home(request):
    return render(request, "todo/home.html")
from .models import Task  # Import your Task model
from django.http import HttpResponse


def create_todo(request):
    if request.method == "POST":
        # Get data from the form
        text = request.POST.get("text")
        category = request.POST.get("category")
        status = request.POST.get("status", "TODO")  # Default to "TODO" if not provided
        due_date = request.POST.get("due_date")
        assigned_to = request.POST.get("assigned_to")

        # Create a new Task item
        Task.objects.create(
            text=text,
            category=category,
            status=status,
            due_date=due_date,
            assigned_to=assigned_to
        )

        # Redirect to a success page or the main task list
        return redirect("task_list")  # Replace 'task_list' with your URL name for the list view

    # Render the form template if the request is GET
    return render(request, "todo/create_todo.html")
def welcome_page(request):
    return render(request, 'todo/welcome.html')

def sign_in(request):
    return render(request, 'todo/sign_in.html')

def register(request):
    return render(request, 'todo/register.html')