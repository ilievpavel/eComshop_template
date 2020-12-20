from django.contrib.auth import logout
from django.urls import path

from users.views import register_user, user_profile, login_user, logout_user

urlpatterns = [
    path('register/', register_user, name='register'),
    path('profile/<int:pk>/', user_profile, name='current user profile'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
]
