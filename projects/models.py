from django.db import models

# Create your models here.
from accounts.models import CustomUser


class Project(models.Model):

    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
    )

    client = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE
    )

    title = models.CharField(max_length=200)

    description = models.TextField()

    budget = models.IntegerField()

    deadline = models.DateField()

    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        default='Pending'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    project_file = models.FileField(
    upload_to='project_files/',
    blank=True,
    null=True
)
    deadline = models.DateField()