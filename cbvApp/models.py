from django.db import models


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=20)
    score = models.IntegerField()

    def __str__(self):
        return self.id + self.name + self.score
