"""
URL configuration for first_pro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

import os
from django.contrib import admin
from django.urls import path, include
from first_app import views 

from api import views
from first_app.user_register import user_register  # Import from the first_app package
from first_app.models import Service
from first_app.services_views import vehicle_list_with_service
from api.views import PurchasedClientsView

urlpatterns = [
    # ... other URL patterns
    #path('login',views.login_user,name = 'login'),

    path('admin/', admin.site.urls),  # Include admin URLs once

    path('api/', include('api.urls')),  # Include API URLs


    # ... other non-API URL patterns for first_app/views.py
    path('', include('first_app.urls')),  # For non-API views

    #path('user_register/', user_register, name='user_register'),

    #path('service/', vehicle_list_with_service, name='service'),
    #path('logout/', views.logout_view,name='logout'),

    # Use PurchasedClientsView (existing API view) for the API endpoint
    #path('clients/', PurchasedClientsView.as_view(), name='clients'),  # Use .as_view()

]




"""

ORIGINLA URL PATTERN:
=====================

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login', include('first_app.urls')),
    path('login',views.login_user,name = 'login'),
    #path("index/", views.index, name="index"),
    path('clients/', views.purchased_clients, name='clients'),
    path('clients/register', views.register, name='register'),
    path('user_register/', user_register, name='user_register'),
    path('my_view/', views.my_view, name='my_view'),
    path('logout/', views.logout_view, name='logout'),  # Name your URL pattern 'logout'
    path('service/', vehicle_list_with_service, name='service'),


    ]
"""

"""
working urls:
http://127.0.0.1:8000/clients/registerhttp://127.0.0.1:8000/clients/register
http://127.0.0.1:8000/clients/
http://127.0.0.1:8000/clients/register
http://127.0.0.1:8000/service/
http://127.0.0.1:8000/login
"""