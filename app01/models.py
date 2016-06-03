from __future__ import unicode_literals
import datetime
from django.utils import timezone

from django.db import models

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
    def __unicode__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __unicode__(self):
        return self.question

#class Reporter(models.Model):
#    full_name = models.CharField(max_length=70)
#    email = models.CharField(max_length=70)
#    address = models.CharField(max_length=70)
#    create_data = models.DateTimeField()
#    
#    def was_published_recently(self):
#        return self.create_data >= timezone.now() - datetime.timedelta(days=1)
#    was_published_recently.admin_order_field = 'create_data'
#    was_published_recently.boolean = True
#    was_published_recently.short_description = 'Published recently?'
#
#    def __unicode__(self):
#        return self.full_name
#
#class Article(models.Model):
#    pub_date = models.DateField()
#    headline = models.CharField(max_length=200)
#    content = models.TextField()
#    reporter = models.ForeignKey(Reporter)
#    
#    def __unicode__(self):
#        return self.headline
