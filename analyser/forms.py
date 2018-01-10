from django import forms
from django.utils import timezone

from tracker.models import Board, Spending


class SpendingForm(forms.ModelForm):
    date = forms.DateField(widget=forms.SelectDateWidget(), initial=timezone.now())

    class Meta:
        model = Spending
        fields = ('name', 'cost', 'category', 'is_income')


class BoardForm(forms.ModelForm):

    class Meta:
        model = Board
        fields = ('name',)
