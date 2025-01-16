from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm
from .models import Profile
from django.contrib.auth import logout

from .forms import SignupForm












# Create your views here.

def login(request):
    return render(request, 'UserApp/login.html')  # Render the login template.


@login_required
def update_profile(request):
    try:
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        profile = Profile(user=request.user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('dashboard')  # Redirect to the dashboard after saving
    else:
        form = ProfileForm(instance=profile)

    return render(request, 'pages/update_profile.html', {'form': form})







def register_user(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect( '../login/' )
    else:
        form = SignupForm()

    return render(request, 'UserApp/register_user.html', {
        'form': form
    })  # Render the register_user template.

def logout(request):
    return render(request, 'UserApp/login.html')  # Render the logout template.