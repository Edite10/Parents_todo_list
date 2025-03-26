## Wireframes 
<details open>
<summary>Wireframe - Welcome Page</summary>
  
![Screenshot 2025-03-26 113936](https://github.com/user-attachments/assets/96bef7f5-ea8f-4cb7-8f13-56bd79193865)

</details>

<details>
<summary>Wireframe - Sign in</summary>

![Screenshot 2025-03-26 114651](https://github.com/user-attachments/assets/4cf1ed73-5484-4e5d-b260-abc29ac3347e)


</details>


<details>
<summary>Wireframe - Register</summary>

![Screenshot 2025-03-26 115420](https://github.com/user-attachments/assets/939b8d34-b276-4f22-8ab7-001393a1889b)


</details>

<details>
<summary>Wireframe - Main page and pop up window</summary>

![Screenshot 2025-03-26 115547](https://github.com/user-attachments/assets/55c8efe8-bda3-4bcc-b49d-9c2904060c43)


</details>

<details>
<summary>Wireframe - Sign out</summary>

![Screenshot 2025-03-26 115614](https://github.com/user-attachments/assets/4d408d4a-59cd-4844-b15a-267d938f62f4)


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

