from django.contrib import admin
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'earnings', 'usdt_bonus', 'display_main_balance')  # Use display_main_balance
    list_filter = ('user',)
    search_fields = ('user__username', 'user__email')
    readonly_fields = ('display_main_balance',)  # Use display_main_balance
    fieldsets = (
        (None, {
            'fields': ('user', 'earnings', 'usdt_bonus', 'display_main_balance')
        }),
    )

    # Define a method to compute and display main_balance
    def display_main_balance(self, obj):
        return (obj.earnings + obj.usdt_bonus) * 3
    display_main_balance.short_description = "Main Balance"  # Customize column header in admin

admin.site.register(Profile, ProfileAdmin)
