from django.shortcuts import render, redirect
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
