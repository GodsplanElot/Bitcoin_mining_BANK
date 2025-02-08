from django import forms
from .models import Message

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['recipient', 'subject', 'body']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # Get the current user from the view
        super().__init__(*args, **kwargs)
        if user:
            # Prevent users from selecting themselves as recipient
            self.fields['recipient'].queryset = User.objects.exclude(id=user.id)