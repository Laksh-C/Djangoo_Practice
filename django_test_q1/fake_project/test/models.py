from django.db import models

class Employee(models.Model):
    Employee_name = models.TextField(max_length=25)
    Employee_department = models.CharField(max_length=15)

    def __str__(self):
        return self.Employee_name+' '+' '+self.Employee_department