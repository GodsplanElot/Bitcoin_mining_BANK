"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404
from pages.views import custom_404_view  # Import your custom 404 view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('user_profiles.urls')),
    path('', include('UserApp.urls')),  # Include the UserApp app's URLs
    path('', include('pages.urls')),  # Include the pages app's URLs
    path('', include('admin_features.urls')),
     path('support/', include('support.urls')), #Include the support app urls
    
]


# Assign the custom 404 view (MUST be placed after urlpatterns)
handler404 = custom_404_view

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)