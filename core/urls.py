from django.urls import path
from core.views import *

urlpatterns = [
    path('auth/register/', Registration.as_view(), name='registration'),
    path('auth/login/', LoginView.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='user_profile'),
    path('profile/update/', UserProfileUpdateView.as_view(), name='user_profile_update')
]
