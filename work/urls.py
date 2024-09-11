from .views import *
from django.urls import path
from uuid import UUID

urlpatterns = [
    path('work-experiences/', WorkExperienceListView.as_view(), name='work-experience-list'),
    path('work-experiences/create/', WorkExperienceCreateView.as_view(), name='work-experience-create'),
    path('work-experiences/<uuid:pk>/', WorkExperienceDetailView.as_view(), name='work-experience-detail'),
    path('work-experiences/<uuid:pk>/edit/', WorkExperienceEditView.as_view(), name='work-experience-edit'),
    path('work-experiences/<uuid:pk>/delete/', WorkExperienceDeleteView.as_view(), name='work-experience-delete'),
]

