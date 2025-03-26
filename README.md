## Wireframes 
<details open>
<summary>Wireframe - Welcome Page</summary>
  
![Screenshot 2025-03-26 140150](https://github.com/user-attachments/assets/2c00e1fb-9762-48af-82a9-70b3a14ddc61)

</details>

<details>
<summary>Wireframe - Sign in</summary>

![Screenshot 2025-03-26 140822](https://github.com/user-attachments/assets/bbc0a8f5-6f2d-4842-896f-003a1e6e4e2c)

</details>

<details>
<summary>Wireframe - Register</summary>

![Screenshot 2025-03-26 140723](https://github.com/user-attachments/assets/b7257e43-e055-4dce-91e6-07351ebb770c)



</details>

<details>
<summary>Wireframe - Main page and pop up window</summary>

![Screenshot 2025-03-26 140459](https://github.com/user-attachments/assets/dec6576f-a039-472f-8fa1-8765198809d7)


</details>

<details>
<summary>Wireframe - Sign out</summary>

![Screenshot 2025-03-26 140649](https://github.com/user-attachments/assets/97457920-760a-4dd3-898d-d4b9f7d98286)



</details>

## Data model example

```
from django.db import models

class Task(models.Model):
    CATEGORY_CHOICES = [
        ('CHORES', 'Chores'),
        ('KIDS', 'Kids'),
        ('ERRANDS', 'Errands'),
        ('SELF_CARE', 'Self-Care'),
    ]
    
    STATUS_CHOICES = [
        ('TODO', 'To Do'),
        ('IN_PROGRESS', 'In Progress'),
        ('DONE', 'Done'),
    ]
    
    text = models.CharField(max_length=255)  # Task description
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)  # Category
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='TODO')  # Status of the task
    due_date = models.DateTimeField(null=True, blank=True)  # Optional due date
    assigned_to = models.CharField(max_length=50, null=True, blank=True)  # e.g., "Mom", "Dad", or "Kid 1"
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set on creation
    updated_at = models.DateTimeField(auto_now=True)  # Automatically set on update
    
    def __str__(self):
        return f"{self.text} ({self.status})"

    class Meta:
        verbose_name = "Task"
        verbose_name_plural = "Tasks"
        ordering = ['created_at']

```
#### Explanation opf the Model Fields

- `text:` The description of the task (e.g., “Buy groceries”).

- `category:` A choice field for the task category (e.g., “Chores”, “Kids”).

- `status:` A choice field to track the task’s status (e.g., "To Do", "In Progress", "Done").

- `due_date:` Optional field to set a due date for the task.

- `assigned_to:` A field to track who is assigned to the task (e.g., "Mom", "Dad", "Kid 1").

- `created_at:` Automatically captures when the task was created.

- `updated_at:` Automatically updates when the task is modified.

