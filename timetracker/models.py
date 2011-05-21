from django.db import models
from django.contrib import admin
from datetime import datetime, timedelta


class Project(models.Model):

    name = models.CharField(max_length="20")
    hourly_wage = models.IntegerField(default="50")
    currency = models.CharField(max_length="3", default="GBP")

    def __unicode__(self):
        return self.name


class TimeEntry(models.Model):

    project = models.ForeignKey(Project)
    start_time = models.DateTimeField()
    duration_in_minutes = models.IntegerField()
    task_description = models.CharField(max_length="120", default="", blank=True)

    class __Meta__:
        ordering = ['-start_time']

    def end_time(self):
        delta = timedelta(minutes=self.duration_in_minutes)
        return self.start_time + delta


admin.site.register(Project)
admin.site.register(TimeEntry)
