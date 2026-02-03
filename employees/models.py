from django.db import models

from django.contrib.auth.models import User

class Employee(models.Model):

    name = models.CharField(max_length=255)

    department = models.CharField(max_length=255)

    designation = models.CharField(max_length=255)

    salary = models.PositiveIntegerField()

    email = models.EmailField()

    date_of_joining = models.DateField()

    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)