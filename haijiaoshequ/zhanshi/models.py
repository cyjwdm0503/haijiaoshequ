# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class TestModel(models.Model):
    pub_date  = models.DateField()
    head_line = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.pub_date+" "+self.head_line+""+self.content;


# Create your models here.
