from django.urls import path
from . import views

urlpatterns = [
    path('create-user/', views.create_user, name='create_user'),
    path('check-user/', views.check_user, name='check_user'),
    path('signup/',views.signup_view, name='signup')
]
