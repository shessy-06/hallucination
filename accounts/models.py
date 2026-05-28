from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser



class CustomUser(AbstractUser):

    ROLE_CHOICES = (
        ('client', 'Client'),
        ('editor', 'Editor'),
        ('admin', 'Admin'),
    )

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default='client'
    )

    phone = models.CharField(
        max_length=15,
        blank=True,
        null=True
    )

    profile_image = models.ImageField(
        upload_to='profiles/',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.username