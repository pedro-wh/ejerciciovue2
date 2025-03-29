from django.db import models

# Create your models here.
class Column(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Todo(models.Model):
    column = models.ForeignKey(Column, on_delete=models.CASCADE, related_name='todos')
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name