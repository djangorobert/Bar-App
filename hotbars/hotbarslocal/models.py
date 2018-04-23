# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

# Create your models here.


class Bar(models.Model):
    name = models.CharField(max_length=100)
    street = models.TextField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    city = models.CharField(blank=True, max_length=50)
    zipCode = models.IntegerField(blank=True, null=True)
    state = models.CharField(blank=True, null=True, max_length=10)
    country = models.CharField(blank=True, null=True, max_length=10)
    telephone = models.IntegerField(blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    user = models.ForeignKey(User, default=1)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('hotbarslocal:bar_detail', kwargs={'pk': self.pk})


class Drink(models.Model):
    name = models.CharField(max_length=50, null=True)
    description = models.TextField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to="DrinkPictures", blank=True, null=True)

    price = models.DecimalField('Dollar amount', max_digits=8, decimal_places=2, blank=True)
    user = models.ForeignKey(User)
    date = models.DateTimeField(auto_now_add=True, blank=True)
    image = models.ImageField(upload_to='mybars', blank=True, null=True)
    bar = models.ForeignKey(Bar, null=True)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('hotbarslocal:drink_detail', kwargs={'pkr': self.bar.pk, 'pk': self.pk})

class Review(models.Model):
    RATING_CHOICES = ((1, 'one'), (2, 'two'), (3, 'three'), (4, 'four'), (5, 'five'))
    rating = models.PositiveSmallIntegerField('Rating (stars)', blank=False, default=3, choices=RATING_CHOICES)
    comment = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User)
    date = models.DateTimeField(auto_now_add=True, blank=True)

class BarReview(Review):
    bar = models.ForeignKey(Bar)