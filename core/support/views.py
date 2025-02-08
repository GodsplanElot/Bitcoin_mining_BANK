from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import MessageForm
from .models import Message

# Create your views here.

def inbox(request):
    messages_received = Message.objects.filter(recipient=request.user).order_by('-timestamp')
    return render(request, 'support/inbox.html', {'messages_received': messages_received})


def sent_messages(request):
    messages_sent = Message.objects.filter(sender=request.user).order_by('-timestamp')
    return render(request, 'support/sent_messages.html', {'messages_sent': messages_sent})


def send_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.save()
            messages.success(request, 'Message sent successfully!')
            return redirect('support:inbox')
    else:
        form = MessageForm()
    return render(request, 'support/send_message.html', {'form': form})