from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .forms import MessageForm
from .models import Message

# Create your views here.
@login_required
def inbox(request):
    messages_received = Message.objects.filter(recipient=request.user).order_by('-timestamp')
    return render(request, 'support/inbox.html', {'messages_received': messages_received})

@login_required
def sent_messages(request):
    messages_sent = Message.objects.filter(sender=request.user).order_by('-timestamp')
    return render(request, 'support/sent_messages.html', {'messages_sent': messages_sent})

def superuser_required(user):
    return user.is_superuser  # Only allows superusers

@login_required
@user_passes_test(superuser_required)  # Apply restriction
def send_message(request):
    form = MessageForm(request.POST or None, user=request.user)
    
    if not request.user.is_superuser:
        form.fields['recipient'].queryset = User.objects.filter(is_superuser=True)
    else:
        form.fields['recipient'].queryset = User.objects.all()

    if request.method == 'POST' and form.is_valid():
        message = form.save(commit=False)
        message.sender = request.user
        message.save()
        messages.success(request, 'Message sent successfully!')
        return redirect('support:inbox')

    return render(request, 'support/send_message.html', {'form': form})