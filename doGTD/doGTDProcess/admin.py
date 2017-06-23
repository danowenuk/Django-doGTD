# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from doGTDProcess.models import Action, Project, List

admin.site.register(Action)
admin.site.register(Project)
admin.site.register(List)
