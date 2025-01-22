from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from UserApp.models import Profile

# Create your views here.
def index(request):
    return render(request, 'pages/index.html')  # Render the index template.

@login_required(login_url="/login")
def dashboard(request):
    # Fetch the logged-in user's profile
    profile = Profile.objects.get(user=request.user)
    context = {
        'user': request.user,  # User object
        'profile': profile     # Profile object with balances
    }
    return render(request, 'pages/dashboard.html', context)  # Render the dashboard template.

@login_required(login_url="/login")
def transaction_list(request):
    return render(request, 'pages/transaction_list.html')  # Render the transaction_list template.
@login_required(login_url="/login")
def my_profile(request):

    return render(request, 'pages/my_profile.html', {'profile': Profile}, )  # Render the my_profile template.

@login_required(login_url="/login")
def customer_support(request):

    profile = Profile.objects.get(user=request.user)
    context = {
        'user': request.user,  # User object
        'profile': profile     # Profile object with balances
    }
    return render(request, 'pages/customer_support.html', context)  # Render the customer_support template.

def about(request):
    return render(request, 'pages/about.html')  # Render the about template.
def privacy_policy(request):
    return render(request, 'pages/privacy_policy.html')  # Render the privacy_policy template.
