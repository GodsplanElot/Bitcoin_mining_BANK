from django.shortcuts import render

# Create your views here.

def register_user(request):
    return render(request, 'UserApp/register_user.html')  # Render the register_user template.