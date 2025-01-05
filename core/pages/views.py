from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'pages/index.html')  # Render the index template.
def dashboard(request):
    return render(request, 'pages/dashboard.html')  # Render the dashboard template.
def hashPowerAll(request):
    return render(request, 'pages/hashPowerAll.html')  # Render the dashboard template.