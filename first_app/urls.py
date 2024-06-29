from django.urls import path
from first_app import views
from first_app.user_register import user_register  # Import from the first_app package
from first_app.services_views import vehicle_list_with_service

#app_name = 'first_app'
urlpatterns = [
    path('login',views.login_user,name = 'login'),
    path("index/", views.index, name="index"),
    path('clients/', views.purchased_clients, name='clients'),
    path('clients/register', views.register, name='register'),
    path('user_register/', user_register, name='user_register'),
    path('my_view/', views.my_view, name='my_view'),
    path('logout/', views.logout_view, name='logout'),  # Name your URL pattern 'logout'
    path('service/', vehicle_list_with_service, name='service'),


    ]  


