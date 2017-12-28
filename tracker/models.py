from django.contrib import settings
from django.db import models

from djmoney.models.fields import MoneyField


class Progile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)


class Board(models.Model):
    owner = models.ForeignKey(Progile)
    name = models.CharField(max_length=150)
    date_create = models.DateTimeField()
    date_updated = models.DateTimeField()
    # add currency field


class Category(models.Model):
    board = models.ForeignKey(Board)
    name = models.CharField(max_length=150)


class SubCategory(models.Model):
    board = models.ForeignKey(Board)
    category = models.ForeignKey(Category)
    name = models.CharField(max_length=150)


class Spending(models.Model):
    board = models.ForeignKey(Board)
    category = models.ForeignKey(Category)
    sub_category = models.ForeignKey(SubCategory)
    name = models.CharField(max_length=150)
    cost = MoneyField(decimal_places=2, default_currency='PLN', max_digits=11)
    is_income = models.BooleanField(default=False)
