from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    path('', views.index, name='index'),  # Home page
    path('dashboard/', views.dashboard, name='dashboard'),  # Dashboard
    path('hashPowerAll/', views.hashPowerAll, name='hashPowerAll'),  # hashPowerAll
]