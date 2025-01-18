from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm
from django.contrib import messages

# Create your views here.


@login_required
def update_profile(request):
    user_profile = request.user.user_profile
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated successfully!')
            return redirect('/my_profile/')
    else:
        form = UserProfileForm(instance=user_profile)

    return render(request, 'user_profiles/update_profile.html', {'form': form})
