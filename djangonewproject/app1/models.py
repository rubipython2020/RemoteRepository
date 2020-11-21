from django.db import models


class position(models.Model):
    title=models.CharField(max_length=50)

    def __str__(self):
        var = self.title
        return var


class Employee(models.Model):
    fullname=models.CharField(max_length=100)
    emp_code=models.CharField(max_length=100)
    mobile=models.CharField(max_length=11)
    position=models.ForeignKey(position,models.CASCADE)
