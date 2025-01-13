from django.contrib import admin
from .models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'earnings', 'usdt_bonus', 'main_balance')
    list_editable = ('earnings', 'usdt_bonus', 'main_balance')


