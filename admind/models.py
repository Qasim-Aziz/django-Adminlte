from django.db import models

class Employee(models.Model):

    name = models.CharField(max_length=50)
    post = models.CharField(max_length=50)
    office = models.CharField(max_length=100)
    age = models.IntegerField()
    joining = models.DateField(auto_now_add=True)
    salary = models.BigIntegerField(blank=False)

    