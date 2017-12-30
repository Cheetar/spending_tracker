from django.conf import settings
from django.db import models

from djmoney.models.fields import MoneyField


class Profile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)


class Board(models.Model):
    id = models.AutoField(primary_key=True)
    owner = models.ForeignKey(Profile, on_delete=models.PROTECT)
    name = models.CharField(max_length=150)
    datetime_created = models.DateTimeField(auto_now_add=True)
    # add currency field

    @property
    def spendings(self):
        return Spending.objects.all().filter(board=self)

    def __str__(self):
        return self.name


class Category(models.Model):
    board = models.ForeignKey(Board, on_delete=models.PROTECT)
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class SubCategory(models.Model):
    board = models.ForeignKey(Board, on_delete=models.PROTECT)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Sub Category'
        verbose_name_plural = 'Sub Categories'


class Spending(models.Model):
    board = models.ForeignKey(Board, on_delete=models.PROTECT)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    sub_category = models.ForeignKey(SubCategory, on_delete=models.PROTECT, blank=True, null=True)
    name = models.CharField(max_length=150)
    cost = MoneyField(decimal_places=2, default_currency='PLN', max_digits=11)
    date = models.DateField(auto_now_add=True)
    is_income = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['date']
