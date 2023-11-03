from django.urls import path
from .views import LoginView, LogoutView, RegistrationView

urlpatterns = [
    path('sign-up/', RegistrationView.as_view(), name='sign_up'),
    path('sign-in/', LoginView.as_view(), name='sign_in'),
    path('sign-out/', LogoutView.as_view(), name='sign_out'),
]
