# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class Context(models.Model):
    GTD_CONTEXTS = (
        ('Ph', 'Phone Call'),
        ('PC', 'PC Work'),
        ('Desk', 'Desk Work'),
    )
    context = models.CharField(max_length=5, choices=GTD_CONTEXTS)

 
class Tag(models.Model):
    GTD_TAG = (
        ('P1', 'Priority 1'),
        ('P2', 'Priority 2'),
        ('P3', 'Priority 3'),
        ('RD', 'Read'),
        ('MGR', 'Manager'),
        ('TODO', 'To do'),
        ('CRIT', 'Critical'),
        ('IMP', 'Important'),
        ('QU', 'Question'),
        ('PSNL', 'Personal'),
        ('IDEA', 'Idea'),
    )
    tag = models.CharField(max_length=5, choices=GTD_TAG)


class List(models.Model):
    list = models.CharField(max_length=100)
    
    def __str__(self):
        return self.list

class Project(models.Model):
    project = models.CharField(max_length=100)
        
    def __str__(self):
        return self.project

class Action(models.Model):
    ACTION_STATUS = (
        (0, 'Open'),
        (1, 'In-progress'),
        (2, 'Closed'),
        (3, 'Deferred'),
        (4, 'Delegated'),
        (5, 'Pending'),
        (6, 'On Hold'),
        (9, 'Cancelled'),
    )
    
    HORIZON = (
        (0, 'Ground'),
        (1, 'Level 1'),
        (2, 'Level 2'),
        (3,  'Level 3'),
        (4, 'Level 4'),
        (5, 'Level 5'),
    )
    title = models.CharField(max_length=140)
    description = models.TextField(blank=True)
    oneNoteReference = models.URLField(blank=True)
    outlookReference = models.URLField(blank=True)
    date = models.DateTimeField()
    dateModified = models.DateTimeField(auto_now=True, auto_now_add=False)
    source = models.CharField(max_length=100, blank=True)
    status = models.IntegerField(choices=ACTION_STATUS, default=0)
    tags = models.ManyToManyField(Tag, blank=True)
    context = models.TextField(default="", help_text="Comma seperated list of contexts")
    contexts = models.ManyToManyField(Context, blank=True)
    lists = models.ManyToManyField(List, blank=True)
    project = models.ManyToManyField(Project, blank=True)
    horizon = models.IntegerField(choices=HORIZON, default=0)
    delegatedTo = models.CharField(max_length=100, blank=True)
    
    def __str__(self):
        return self.title