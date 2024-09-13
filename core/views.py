import logging
import traceback
from venv import logger

from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import RegistrationSerializer, LoginSerializer, UserProfileSerializer
from rest_framework.response import Response
from django.db import transaction
from rest_framework_simplejwt.tokens import RefreshToken
from common.docs import *
from rest_framework.permissions import AllowAny, IsAuthenticated
from social_django.utils import load_strategy, load_backend
from social_core.backends.google import GoogleOAuth2
from social_core.exceptions import AuthException
from django.conf import settings
from django.contrib.auth import login


class Registration(APIView):
    serializer_class = RegistrationSerializer
    permission_classes = [AllowAny]

    @registration_docs()
    @transaction.atomic()
    def post(self, request):
        try:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                user = serializer.save()

                return Response({'id': user.id, 'message': "User registered successfully"}, status=status.
                                HTTP_201_CREATED)
            return Response({'errors': 'serializer.errors', 'data': None}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logging.error(f"Error occurred: {e}")
            return Response({'message': f'Internal Server Error: {str(e)}', 'data': None},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class LoginView(TokenObtainPairView):
    serializer_class = LoginSerializer

    @login_docs()
    @transaction.atomic()
    def post(self, request, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid():
                user = serializer.validated_data.get('user')

                # Generate refresh and access tokens
                refresh = RefreshToken.for_user(user)
                access = refresh.access_token

                tokens = {
                    "refresh": str(refresh),
                    "access": str(access)
                }
                return Response(tokens, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.error(f"Error occurred during password reset: {e}")
            return Response({'message': 'Internal Server Error', 'data': None},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class UserProfileView(APIView):
    serializer_class = UserProfileSerializer

    @user_profile_docs()
    def get(self, request):
        try:
            user = request.user
            if not user or not user.is_authenticated:
                return Response({'message': 'User not authenticated', 'data': None},
                                status=status.HTTP_401_UNAUTHORIZED)
            serializer = self.serializer_class(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            logging.error(f"Error occurred: {e}")
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class UserProfileUpdateView(APIView):
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    @user_profile_docs()
    def put(self, request):
        try:
            user = request.user
            # Partial update allows updating only a subset of fields
            serializer = self.serializer_class(user, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logging.error(f"Error occurred during profile update: {e}")
            logging.error(traceback.format_exc())  # Add traceback logging for more details
            return Response({'message': 'An unexpected error occurred'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class GoogleOAuth2Login(APIView):
    permission_classes = [AllowAny]

    @google_login_docs()
    def post(self, request):
        try:
            strategy = load_strategy(request)
            backend = load_backend(strategy, 'google-oauth2', None)

            try:
                # Get the access token from the request data
                user = backend.do_auth(request.data.get('access_token'))
            except AuthException as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

            if user and user.is_active:
                # Login the user and create a JWT token
                login(request, user)
                refresh = RefreshToken.for_user(user)

                return Response({
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                })
            else:
                return Response({"error": "Authentication failed"}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logging.error(f"Error occurred: {e}")
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
