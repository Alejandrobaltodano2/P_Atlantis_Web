#
from django.urls import path

from . import views

app_name = "users_app"

urlpatterns = [
    path(
        'register/', 
        views.RegisterUserView.as_view(),
        name='user-register',
    ),path(
        'login/', 
        views.LoginUser.as_view(),
        name='user-login',
    ),
      path(
        'user-verification/<pk>/', 
        views.CodeVerificationView.as_view(),
        name='user-verification',
    ),
    path(
        'logout/',
        views.LogoutView.as_view(),
        name="logout"
    )
    
]