from django.db import models
from django.contrib.auth.models import User
class Question(models.Model):
    header = models.CharField(max_length=50)
    content = models.CharField(max_length=150)
    author = models.ForeignKey(User)
    create_date = models.DateField(auto_now_add=True)

class Answer(models.Model):
    content = models.CharField(max_length=150)
    question = models.ForeignKey(Question)
    author = models.ForeignKey(User)
    create_date = models.DateField(auto_now_add=True)
    is_right = models.NullBooleanField()


