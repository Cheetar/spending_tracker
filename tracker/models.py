from datetime import datetime

from django.conf import settings
from django.db import models

from djmoney.models.fields import MoneyField


class Progile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class Board(models.Model):
    owner = models.ForeignKey(Progile, on_delete=models.PROTECT)
    name = models.CharField(max_length=150)
    date_create = models.DateTimeField()
    date_updated = models.DateTimeField()
    # add currency field


class Category(models.Model):
    board = models.ForeignKey(Board, on_delete=models.PROTECT)
    name = models.CharField(max_length=150)


class SubCategory(models.Model):
    board = models.ForeignKey(Board, on_delete=models.PROTECT)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    name = models.CharField(max_length=150)


class Spending(models.Model):
    board = models.ForeignKey(Board, on_delete=models.PROTECT)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    sub_category = models.ForeignKey(SubCategory, on_delete=models.PROTECT)
    name = models.CharField(max_length=150)
    cost = MoneyField(decimal_places=2, default_currency='PLN', max_digits=11)
    date = models.DateField(default=datetime.now())
    is_income = models.BooleanField(default=False)
