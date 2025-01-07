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
    path('login/', views.login, name='login'),  # login
    path('about/', views.about, name='about'),  # about
    path('privacy_policy/', views.privacy_policy, name='privacy_policy'),  # privacy_policy
    path('logout/', views.logout, name='logout'),  # logout
]