from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth import get_user_model
from work.models import WorkExperience

User = get_user_model()

class WorkExperienceAPITestCase(APITestCase):

    def setUp(self):
        # Create a user with email and password (no username)
        self.user = User.objects.create_user(
            email="testuser@example.com",
            password="password123"
        )
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

        # Create a work experience instance
        self.work_experience = WorkExperience.objects.create(
            user=self.user,
            job_title="Software Engineer",
            company_name="Tech Corp",
            location="Remote",
            job_type=WorkExperience.FULL_TIME,
            start_date="2022-01-01",
            end_date="2023-01-01",
            description="Worked on developing APIs."
        )

        # Use the correct URL names defined in your urlpatterns
        self.list_url = reverse('work-experience-list')
        self.create_url = reverse('work-experience-create')
        self.detail_url = reverse('work-experience-detail', kwargs={'pk': self.work_experience.pk})
        self.edit_url = reverse('work-experience-edit', kwargs={'pk': self.work_experience.pk})
        self.delete_url = reverse('work-experience-delete', kwargs={'pk': self.work_experience.pk})

    def test_list_work_experiences(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_work_experience(self):
        data = {
            "job_title": "Product Manager",
            "company_name": "Product Inc",
            "location": "New York",
            "job_type": "Full-time",
            "start_date": "2023-02-01",
            "end_date": "2024-02-01",
            "description": "Managing product development."
        }
        response = self.client.post(self.create_url, data)
#        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#        self.assertEqual(WorkExperience.objects.count(), 2)

    def test_get_work_experience_detail(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['job_title'], 'Software Engineer')

    def test_edit_work_experience(self):
        data = {
            "job_title": "Senior Software Engineer",
            "description": "Updated description"
        }
        response = self.client.put(self.edit_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.work_experience.refresh_from_db()
#        self.assertEqual(self.work_experience.job_title, "Senior Software Engineer")
#        self.assertEqual(self.work_experience.description, "Updated description")

    def test_delete_work_experience(self):
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(WorkExperience.objects.count(), 0)
