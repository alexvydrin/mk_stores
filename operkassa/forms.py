from django import forms

from .models import Oper

class OperForm(forms.ModelForm):

    class Meta:
        model = Oper
        fields = ('date', 'sum_debet', 'sum_credit', 'text',)