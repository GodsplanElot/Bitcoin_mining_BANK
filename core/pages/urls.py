from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    path('', views.index, name='index'),  # Home page
    path('dashboard/', views.dashboard, name='dashboard'),  # Dashboard
    path('hashPowerAll/', views.hashPowerAll, name='hashPowerAll'),  # hashPowerAll
    path('transaction_list/', views.transaction_list, name='transaction_list'),  # transaction_list
    path('my_profile/', views.my_profile, name='my_profile'),  # my_profile
    path('customer_support/', views.customer_support, name='customer_support'),  # customer_support
    path('register_user/', views.register_user, name='register_user'),  # register_user
]