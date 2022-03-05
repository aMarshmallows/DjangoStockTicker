# -*- coding: utf-8 -*-
# used to interact with the database side
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Stock(models.Model):
    # creates a column in our Stocks database
    ticker = models.CharField(max_length=10)

    # allows ticker name to show up in data base instead of Stock Object
    def __str__(self):
        return self.ticker