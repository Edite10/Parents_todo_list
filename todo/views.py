from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.views import generic
from django.views.generic import ListView
from .models import Task
# Create your views here.


class parent_list(ListView):
    model = Task  # Specify the model to fetch data from
    template_name = "todo/task_list.html"  # Specify the template to render
    context_object_name = "tasks"  # Name of the context variable in the template

    def list(self, **kwargs):
        # Get the list of tasks from the database
        task_list = Task.objects.all()
        return render(self.request, "base.html")


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
        return redirect("view")
    # Render the form template if the request is GET
    return render(request, "todo/create_todo.html")
def welcome_page(request):
    return render(request, 'todo/welcome.html')

def sign_in(request):
    return render(request, 'todo/sign_in.html')


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
        return redirect("view") 

    # Render the form template with the current task data
    return render(request, "todo/update_todo.html", {"task": task})


def task_detail(request, task_id):
    # Retrieve the task object or return a 404 if not found
    task = get_object_or_404(Task, id=task_id)

    # Render the task detail template with the task data
    return render(request, "todo/task_detail.html", {"task": task})

def task_delete(request, task_id):
    # Retrieve the task object or return a 404 if not found
    task = get_object_or_404(Task, id=task_id)

    if request.method == "POST":
        # Delete the task from the database
        task.delete()
        # Redirect to the task list after deletion
        return redirect("view")

    # Render a confirmation page
    return render(request, "todo/task_delete.html", {"task": task})
