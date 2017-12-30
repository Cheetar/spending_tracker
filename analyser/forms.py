from django import forms

from tracker.models import Board, Spending


class SpendingForm(forms.ModelForm):

    class Meta:
        model = Spending
        fields = ('name', 'cost', 'category', 'is_income')


class BoardForm(forms.ModelForm):

    class Meta:
        model = Board
        fields = ('name',)
