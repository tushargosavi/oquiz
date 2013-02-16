from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Question(models.Model):
    user = models.ForeignKey(User)
    numLikes = models.IntegerField()
    numUnLikes = models.IntegerField()
    added = models.DateField()
    opt1 = models.TextField()
    opt2 = models.TextField()
    opt3 = models.TextField()
    opt4 = models.TextField()
    opt5 = models.TextField()
    correctOpt = models.IntegerField()

class Answer(models.Model):
    user = models.ForeignKey(User)
    question = models.ForeignKey(Question)
    answer = models.IntegerField()
    numAttempts = models.IntegerField()
