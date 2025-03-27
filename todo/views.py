from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Task

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

def update_todo(request, task_id):
    # Retrieve the task object or return a 404 if not found
    task = get_object_or_404(Task, id=task_id)

    if request.method == "POST":
        # Update the task with the submitted form data
        task.text = request.POST.get("text")
        task.category = request.POST.get("category")
        task.status = request.POST.get("status")
        task.due_date = request.POST.get("due_date")
        task.assigned_to = request.POST.get("assigned_to")
        task.save()  # Save the updated task to the database

        # Redirect to a success page or the task list
        return redirect("task_list")  # Replace 'task_list' with your URL name for the list view

    # Render the form template with the current task data
    return render(request, "todo/update_todo.html", {"task": task})