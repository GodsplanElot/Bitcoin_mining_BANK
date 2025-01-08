from django.shortcuts import render, redirect

from .forms import SignupForm

# Create your views here.

def login(request):
    return render(request, 'UserApp/login.html')  # Render the login template.



def register_user(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect(' /login/ ')
    else:
        form = SignupForm()

    return render(request, 'UserApp/register_user.html', {
        'form': form
    })  # Render the register_user template.

