__author__ = 'jql'

from django.db import models
class AdminPerson(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()