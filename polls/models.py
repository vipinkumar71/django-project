from django.db import models

# Create your models here.
from django.db import models

"""class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)"""


class Poll(models.Model):
    """polls models"""
    title = models.CharField(max_length=255, default='')
    rating = models.IntegerField(default=0)
    description = models.TextField(blank=True, null=True)
    poll_closed = models.BooleanField(default=False)
    logo = models.FileField(upload_to='uploads', blank=True, null=True)

    def __str__(self):
        return self.title
