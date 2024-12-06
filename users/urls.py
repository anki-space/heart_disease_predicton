from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('home/', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('successfully_registered/', views.successfully_registered, name='successfully_registered'),
    path('successfully_logged_in/', views.successfully_logged_in, name='successfully_logged_in'),
    path('signout_profile/', views.signout_profile, name='signout_profile'),
    path('prediction_form/', views.prediction_form, name='prediction_form'),
    path('prediction/', views.prediction, name='prediction'),
    path('result/', views.result, name='result'),
    path('view_history/', views.view_history, name='view_history'),
]