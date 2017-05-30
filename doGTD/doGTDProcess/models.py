# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Action(models.Model):
    title = models.CharField(max_length=140)
    description = models.TextField()
    date = models.DateTimeField()
    
    def __str__(self):
        return self.title