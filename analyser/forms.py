from django import forms

from tracker.models import Spending


class SpendingForm(forms.ModelForm):

    class Meta:
        model = Spending
        fields = ('name', 'cost', 'category', 'sub_category', 'is_income')
