from django.urls import path
from . import views

app_name = 'admin_features'

urlpatterns = [
    path('manipulate/<int:user_id>/', views.manipulate_balance, name='manipulate_balance'),
]
