from django.urls import path
from . import views

app_name = 'UserApp'

urlpatterns = [
    path('register_user/', views.register_user, name='register_user'),  # register_user

]