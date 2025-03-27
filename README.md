
## User Experience (UX)

### Primary Goal

The website will serve as a simple, intuitive, and collaborative to-do list for parents to manage household tasks efficiently. It will have a family-friendly and visually organized interface with a mobile-first design, ensuring accessibility from any device.

### First-Time Users

- New users will find a clean and organized layout that makes it easy to add and manage tasks.
- New users will be able to quickly create an account and set up their first task list.
- New users will receive a brief guided walkthrough of key features (e.g., task creation, reminders, collaboration).
- New users will be able to invite family members to collaborate on shared tasks.
- New users will have the option to customize their to-do board (e.g., colors, categories) to fit their needs.


### Returning Users

- Returning users will automatically see their active tasks upon logging in.
- Returning users will be able to quickly access tasks from their last session without extra steps.
- Returning users will have the ability to filter or search for tasks based on priority, due date, or assignee.
- Returning users will be able to review completed and overdue tasks to track progress.
- Returning users will stay updated with push notifications or reminders for upcoming tasks.

### Collaboration & Family Engagement

- Parents can assign tasks to specific family members, ensuring shared responsibilities.
- Parents and family members can leave comments on tasks to communicate details or updates.
- Parents can track which tasks have been completed by family members.

### Customization & Usability

- Users can drag and drop tasks to update their status quickly.
- Users can customize task categories to fit their unique workflow.
- Users can choose between light and dark modes for better accessibility.
- Users can set recurring tasks for daily, weekly, or monthly chores.

### Mobile Accessibility & Notifications

- The website will be mobile-friendly, allowing parents to manage tasks on the go.
- Users can receive push notifications for task reminders and updates.
- Users will have a quick-add button to create tasks easily from any device.

## Creation Process

1. Stretegy
   - We need a website that is family-friendly and easy to use for busy parents.
   - The interface should be clean, intuitive, and visually organized for quick task management.
   - It should support collaborative features so family members can share responsibilities.
   - The design should be minimalistic but engaging, making daily task tracking stress-free.

2. Scope
   - The website should be fully responsive, working seamlessly across desktop, tablet, and mobile devices.
   - Users should be able to create, edit, and delete tasks effortlessly.
   - Users should be able to set priorities, deadlines, and reminders for their tasks.
   - The website should include a help section with guides on using features efficiently.
  
3. Structural
   - The website will have a table-based layout to display tasks clearly, with columns for task name, status (To-Do, In Progress, Done), and actions.
   - Users can update task status by selecting checkboxes in the corresponding columns.
   - A search bar at the top will allow users to quickly find tasks by keyword.
   - A "Create new task" button will trigger a pop-up form, where users can enter the task name, category, status, and end date.
   - The action buttons (View, Edit, Delete) will allow users to manage tasks efficiently without unnecessary navigation.
   - The website will have a fixed sign-out button for easy access to log out.
   - The design will prioritize clarity and simplicity, making it easy for parents to track, update, and organize their tasks.

4. Skeleton
   - The website will have a main dashboard displaying a table with task names, status columns (To-do, In Progress, Done), and action buttons.
   - Users will be able to check off tasks in the respective status columns to update progress.
   - A search bar will be present at the top to quickly find tasks.
   - A "Create new task" button will open a pop-up form, allowing users to enter task details such as name, category, status, and due date.
   - Each task will have three action buttons:
                     - View (for details
                     - Edit (to modify task information)
                     - Delete (to remove a task)
   - A Sign-out button will be available for account security.
   - The overall design will be clean, minimalistic, and user-friendly, ensuring easy task management for parents.


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

## Surface

### Colour Scheme 

![Screenshot 2025-03-27 134508](https://github.com/user-attachments/assets/7ce31ec4-cabf-4ef7-937b-be9828669b77)


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

