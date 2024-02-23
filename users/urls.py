from django.urls import path
from . import views

app_name = 'users'  # This should be the same as the app_name defined in the main urls.py

urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('logout', views.logout, name='logout'),
]
