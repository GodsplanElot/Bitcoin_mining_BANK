from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
from .forms import LoginForm

app_name = 'UserApp'

urlpatterns = [
    path('register_user/', views.register_user, name='register_user'),  # register_user
    path('login/', auth_views.LoginView.as_view(template_name='UserApp/login.html', authentication_form=LoginForm), name='login'),  # login

]