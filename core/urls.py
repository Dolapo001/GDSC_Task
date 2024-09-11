from django.urls import path
from .views import *


urlpatterns = [
    path('register/', Registration.as_view(), name='student-registration'),
    path('login/', LoginView.as_view(), name='admin-login'),
    path('profile/', UserProfileView.as_view(), name='user-profile'),

]