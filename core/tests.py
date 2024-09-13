from unittest.mock import patch, MagicMock

from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from social_core.exceptions import AuthException

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


class GoogleOAuth2LoginAPITestCase(APITestCase):
    def setUp(self):
        self.url = reverse('google-auth')  # Update with the correct URL name

    @patch('core.views.load_strategy')  # Update with the correct path to load_strategy
    @patch('core.views.load_backend')  # Update with the correct path to load_backend
    @patch('core.views.login')  # Update with the correct path to login
    @patch('core.views.RefreshToken')  # Update with the correct path to RefreshToken
    def test_successful_login(self, mock_refresh_token, mock_login, mock_load_backend, mock_load_strategy):
        # Setup mocks
        mock_strategy = MagicMock()
        mock_load_strategy.return_value = mock_strategy

        mock_backend = MagicMock()
        mock_load_backend.return_value = mock_backend

        mock_user = MagicMock()
        mock_user.is_active = True
        mock_backend.do_auth.return_value = mock_user

        mock_refresh = MagicMock()
        mock_refresh.access_token = 'mock_access_token'
        mock_refresh_token.for_user.return_value = mock_refresh

        # Perform the POST request
        response = self.client.post(self.url, {'access_token': 'mock_access_token'}, format='json')

        # Assert successful response
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('refresh', response.data)
        self.assertIn('access', response.data)
        self.assertEqual(response.data['access'], 'mock_access_token')

    @patch('core.views.load_strategy')  # Update with the correct path
    @patch('core.views.load_backend')  # Update with the correct path
    def test_auth_exception(self, mock_load_backend, mock_load_strategy):
        # Setup mocks
        mock_strategy = MagicMock()
        mock_load_strategy.return_value = mock_strategy

        mock_backend = MagicMock()
        mock_load_backend.return_value = mock_backend

        mock_backend.do_auth.side_effect = AuthException("Authentication error")

        # Perform the POST request
        response = self.client.post(self.url, {'access_token': 'mock_access_token'}, format='json')

        # Assert error response
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
#        self.assertEqual(response.data['error'], 'Authentication error')

    @patch('core.views.load_strategy')  # Update with the correct path
    @patch('core.views.load_backend')  # Update with the correct path
    def test_user_inactive(self, mock_load_backend, mock_load_strategy):
        # Setup mocks
        mock_strategy = MagicMock()
        mock_load_strategy.return_value = mock_strategy

        mock_backend = MagicMock()
        mock_load_backend.return_value = mock_backend

        mock_user = MagicMock()
        mock_user.is_active = False
        mock_backend.do_auth.return_value = mock_user

        # Perform the POST request
        response = self.client.post(self.url, {'access_token': 'mock_access_token'}, format='json')

        # Assert error response
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['error'], 'Authentication failed')

    @patch('core.views.load_strategy')  # Update with the correct path
    @patch('core.views.load_backend')  # Update with the correct path
    def test_exception_handling(self, mock_load_backend, mock_load_strategy):
        # Setup mocks
        mock_strategy = MagicMock()
        mock_load_strategy.return_value = mock_strategy

        mock_load_backend.side_effect = Exception("Unexpected error")

        # Perform the POST request
        response = self.client.post(self.url, {'access_token': 'mock_access_token'}, format='json')

        # Assert server error response
        self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)