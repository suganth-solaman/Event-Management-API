from django.urls import path
from .views import UserRegistrationView, UserLoginView, Test
from knox import views as knox_views


urlpatterns = [
    path('api/register/', UserRegistrationView.as_view(), name='register'),
    path('api/login/', UserLoginView.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('test/', Test.as_view(), name='test'),
]
