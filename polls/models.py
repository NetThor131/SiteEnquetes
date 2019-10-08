# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Pool(models.Model):
    question = models.CharField(max_lenght=200)
    pub_date = models.DateTimeField('date published')
    
class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    choice = models.CharField(max_lenght=200)
    votes = models.IntegerField()