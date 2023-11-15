import datetime
from django.db import models
from django.utils import timezone

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=250)
    publication_date = models.DateTimeField()

    def recent_question(self):
        return self.publication_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.question_text

class Choix(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choix_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choix_text
