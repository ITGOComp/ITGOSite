from django import forms
from .models import checkout

class WithdrawalNoticeForm(forms.ModelForm):
    class Meta:
        model = checkout
        fields = ['username', 'phone', 'mail']
