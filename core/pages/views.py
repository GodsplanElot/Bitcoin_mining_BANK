from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'pages/index.html')  # Render the index template.
def dashboard(request):
    return render(request, 'pages/dashboard.html')  # Render the dashboard template.
def hashPowerAll(request):
    return render(request, 'pages/hashPowerAll.html')  # Render the hashPowerAll.
def transaction_list(request):
    return render(request, 'pages/transaction_list.html')  # Render the transaction_list template.
def my_profile(request):
    return render(request, 'pages/my_profile.html')  # Render the my_profile template.
def customer_support(request):
    return render(request, 'pages/customer_support.html')  # Render the customer_support template.
def register_user(request):
    return render(request, 'pages/register_user.html')  # Render the register_user template.
def login(request):
    return render(request, 'pages/login.html')  # Render the login template.
def about(request):
    return render(request, 'pages/about.html')  # Render the about template.