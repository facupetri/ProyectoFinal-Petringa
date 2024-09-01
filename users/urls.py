from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import *



urlpatterns = [
    path('login/', login_request, name='login'),
    path('register/', register, name='register'),
    path('logout/', LogoutView.as_view(template_name='base/index.html'), name='logout'),
    path('edit-user/', edit_user, name='edit_user'),
    path('change-pass/', CambiarContrasena.as_view(), name='change_pass'),
]
