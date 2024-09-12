from django.urls import path
from .views import *

urlpatterns = [
    path('skills/', SkillListView.as_view(), name='skill-list'),
    path('skills/add/', AddUserSkillView.as_view(), name='add-user-skill'),
    path('skills/', UserSkillListView.as_view(), name='user-skill-list'),
    path('skills/<uuid:pk>/delete/', UserSkillDeleteView.as_view(), name='delete-user-skill'),
    path('users/search/', UserSearchView.as_view(), name='user-search'),
]
