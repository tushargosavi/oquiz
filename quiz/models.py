from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Question(models.Model):
    text = models.TextField()
    opt1 = models.TextField()
    opt2 = models.TextField()
    opt3 = models.TextField()
    opt4 = models.TextField()
    opt5 = models.TextField()
    correctOpt = models.IntegerField()
    user = models.ForeignKey(User)
    added = models.DateField()
    numLikes = models.IntegerField()
    numUnLikes = models.IntegerField()


class Answer(models.Model):
    user = models.ForeignKey(User)
    question = models.ForeignKey(Question)
    answer = models.IntegerField()
    numAttempts = models.IntegerField()
    def __str__(self):
        return "[" + self.user.username + "," +  question.id + "]" 

class Tag(models.Model):
    name = models.CharField(max_length=64, unique=True)
    questions = models.ManyToManyField(Question)
    def __str__(self):
        return self.name
