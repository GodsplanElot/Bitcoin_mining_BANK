from django import forms
from UserApp.models import Profile

class BalanceUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['earnings', 'usdt_bonus', 'main_balance']
