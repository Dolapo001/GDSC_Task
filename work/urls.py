from .views import *
from django.urls import path
from uuid import UUID

urlpatterns = [
    path('experiences/', WorkExperienceListView.as_view(), name='work-experience-list'),
    path('experiences/create/', WorkExperienceCreateView.as_view(), name='work-experience-create'),
    path('experiences/<uuid:pk>/', WorkExperienceDetailView.as_view(), name='work-experience-detail'),
    path('experiences/<uuid:pk>/edit/', WorkExperienceEditView.as_view(), name='work-experience-edit'),
    path('experiences/<uuid:pk>/delete/', WorkExperienceDeleteView.as_view(), name='work-experience-delete'),
]

