from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model

User = get_user_model()


class RegistrationTestCase(APITestCase):
    def setUp(self):
        self.registration_url = reverse('registration')

    def test_registration_success(self):
        data = {
            "email": "testuser@example.com",
            "password": "testpass123",
            "name": "Test User"
        }
        response = self.client.post(self.registration_url, data, format='json')

    def test_registration_fail(self):
        data = {
            "email": "",  # Missing required fields
            "password": "short",
        }
        response = self.client.post(self.registration_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['errors'], 'serializer.errors')


class LoginTestCase(APITestCase):
    def setUp(self):
        self.login_url = reverse('login')
        self.user = User.objects.create_user(email='testuser@example.com', password='testpass123', name="Test User")

    def test_login_success(self):
        data = {
            "email": "testuser@example.com",
            "password": "testpass123"
        }
        response = self.client.post(self.login_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)

    def test_login_fail(self):
        data = {
            "email": "testuser@example.com",
            "password": "wrongpassword"
        }
        response = self.client.post(self.login_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class UserProfileTestCase(APITestCase):
    def setUp(self):
        self.profile_url = reverse('user_profile')
        self.user = User.objects.create_user(email='testuser@example.com', password='testpass123', name="Test User")
        self.client.force_authenticate(user=self.user)  # Authenticate the user

    def test_get_user_profile_success(self):
        response = self.client.get(self.profile_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['email'], self.user.email)

    def test_get_user_profile_unauthorized(self):
        self.client.logout()  # Log the user out
        response = self.client.get(self.profile_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class UserProfileUpdateTests(APITestCase):

    def setUp(self):
        # Create a user and authenticate
        self.user = User.objects.create_user(
            email='jane.doe@example.com',
            name='Jane Doe',
            password='Password123!',
            phone='1234567890'
        )
        self.client.force_authenticate(user=self.user)
        self.profile_update_url = reverse('user_profile_update')  # Ensure this name matches the URL pattern name

    def test_update_user_profile(self):
        profile_picture = SimpleUploadedFile("profile.jpg", b"file_content", content_type="image/jpeg")
        update_data = {
            'name': 'Jane Updated',
            'phone': '0987654321',
            'profile_picture': profile_picture
        }
        response = self.client.put(self.profile_update_url, update_data, format='multipart')
        self.assertTrue('profile_picture' in response.data)
