from django.urls import path
from .views import *

urlpatterns = [
    path('skills/', SkillListView.as_view(), name='skill-list'),
    path('user-skills/add/', AddUserSkillView.as_view(), name='add-user-skill'),
    path('user-skills/', UserSkillListView.as_view(), name='user-skill-list'),
    path('<uuid:pk>/delete/', UserSkillDeleteView.as_view(), name='delete-user-skill'),
    path('users/search/', UserSearchView.as_view(), name='user-search'),

    path('user-interests/', UserInterestsView.as_view(), name='user-interests'),
    path('user-interests/add/', AddUserInterestView.as_view(), name='add-user-interest'),
    path('user-interests/<uuid:pk>/delete/', DeleteUserInterestView.as_view(), name='delete-user-interest'),
    path('interests/', InterestListView.as_view(), name='predefined-interests'),

]
