import datetime

from django.conf import settings
from django.db import models

CATEGORIES = (('Home', 'Home'),
              ('Bills', 'Bills'),
              ('Taxes', 'Taxes'),
              ('Clothes', 'Clothes'),
              ('Shopping', 'Shopping'),
              ('Holidays', 'Holidays'),
              ('Health', "Health"),
              ('Sports', 'Sports'),
              ('Food', 'Food'),
              ('Gifts', 'Gifts'),
              ('Kids', 'Kids'),
              ('Fuel', 'Fuel'),
              ('Transport', 'Transport'),
              ('Entertainment', 'Entertainment'),
              ('Going out', 'Going out'),
              ('Eating out', 'Eating out'),
              ('Other', 'Other'),
              # Income CATEGORIES
              ('Salary', 'Salary'))


class Profile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    @classmethod
    def create(user):
        profile = Profile(user=user)
        profile.save
        return profile

    def __str__(self):
        return str(self.user)


class Board(models.Model):
    id = models.AutoField(primary_key=True)
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)
    name = models.CharField(max_length=150, default="Main board")
    datetime_created = models.DateTimeField(auto_now_add=True)
    currency = models.CharField(default='USD', max_length=30)

    @classmethod
    def create(profile):
        board = Board(owner=profile)
        board.save()
        return board

    @property
    def spendings(self):
        return Spending.objects.all().filter(board=self)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-datetime_created']
        unique_together = ("owner", "name")


class Spending(models.Model):
    id = models.AutoField(primary_key=True)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    category = models.CharField(max_length=50, choices=CATEGORIES)
    name = models.CharField(max_length=150, blank=True)
    cost = models.DecimalField(decimal_places=2, max_digits=11)
    date = models.DateField(default=datetime.date.today)
    is_income = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-date']
