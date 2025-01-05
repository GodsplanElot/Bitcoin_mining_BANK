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