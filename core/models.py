from enum import auto
from secrets import choice
from telnetlib import STATUS
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Topics(models.Model):
    p_key = models.IntegerField(primary_key=True)
    title_topic = models.CharField(max_length=100)
    text_topic = models.CharField(max_length=300)
    
    def __str__(self):
        
        return self.p_key, self.title_topic, self.text_topic

class Users(models.Model):

    p_key_user = models.CharField(max_length=20, primary_key=True)
    name_user = models.CharField(max_length=77)
    password_user = models.CharField(max_length=100)

    def __str__(self):

        return self.p_key_user, self.name_user, self.password_user


class Coments(models.Model):

    key_comment = models.IntegerField(blank=True)
    comment = models.CharField(max_length=77)

    def __str__(self):
        return self.comment
