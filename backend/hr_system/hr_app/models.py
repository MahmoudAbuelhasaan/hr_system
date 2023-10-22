from django.db import models
import uuid
class HR(models.Model):
    id = models.CharField(primary_key=True, max_length=36, unique=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100,unique=True)
    password = models.CharField(max_length=100) 

    def __str__(self):
        return self.name
    


class Employee(models.Model):
    id = models.CharField(primary_key=True, max_length=36, unique=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    employee_id = models.CharField(max_length=20, unique=True)
    department = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Attendance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=20)  # You can use choices for 'present', 'absent', etc.

    def __str__(self):
        return f"{self.employee.name} - {self.date}"




