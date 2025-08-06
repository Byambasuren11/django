from django.urls import path
from .views import create_user, check_user, signup_view, test_api

urlpatterns = [
    path('api/create-user/', create_user, name='create_user'),
    path('api/check-user/', check_user, name='check_user'),
    path('signup/', signup_view, name='signup'),
    path('api/test/', test_api, name='test_api'),  # ← энэ өмнө нь syntax алдаатай байсан
]


