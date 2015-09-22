import datetime

from django.db import models
from django.utils import timezone

#Creating Two Models
#A

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __unicode__(self):
        #TODO: By default, this is the value that is returned to Django Admin, and it must be a string.
        return self.question_text
        #return str(self.pub_date)

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __unicode__(self):
        return self.choice_text