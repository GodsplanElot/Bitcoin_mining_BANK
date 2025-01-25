from django import forms
from user_profiles.models import UserProfile

class BalanceUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['earnings', 'usdt_bonus_amount']
