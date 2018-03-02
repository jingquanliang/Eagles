from __future__ import unicode_literals

from django.db import models

from entity.AdminUser import *

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    sound = models.CharField(max_length=30,null=True,default='')

    def speak(self):
        return "dlsjf"



