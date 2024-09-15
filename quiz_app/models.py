from django.db import models

class Question(models.Model):
    text = models.TextField()
    answer = models.CharField(max_length=255)
    used = models.BooleanField(default=False)

    def __str__(self):
        return self.text

class Team(models.Model):
    name = models.CharField(max_length=100)
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.name
