from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import BalanceUpdateForm

# Create your views here.


def is_superuser(user):
    return user.is_superuser

@user_passes_test(is_superuser)
def manipulate_balance(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        form = BalanceUpdateForm(request.POST, instance=user.profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Balance updated successfully!')
    else:
        form = BalanceUpdateForm(instance=user.profile)


    return render(request, 'admin_features/manipulate_balance.html', {'form': form, 'user': user})
