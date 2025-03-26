from django.db import models

# Create your models here.


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
    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES
        )  # Category
    status = models.CharField(
        max_length=15,
        choices=STATUS_CHOICES,
        default='TODO'
        )  # Status of the task
    due_date = models.DateTimeField(null=True, blank=True)  # Optional due date
    assigned_to = models.CharField(
        max_length=50,
        null=True,
        blank=True
        )  # e.g., "Mom", "Dad", or "Kid 1"
    created_at = models.DateTimeField(
        auto_now_add=True
        )  # Automatically set on creation
    updated_at = models.DateTimeField(
        auto_now=True
        )  # Automatically set on update

    def __str__(self):
        return f"{self.text} ({self.status})"

    class Meta:
        verbose_name = "Task"
        verbose_name_plural = "Tasks"
        ordering = ['created_at']
