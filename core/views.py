import logging
from venv import logger
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import RegistrationSerializer, LoginSerializer, UserProfileSerializer
from rest_framework.response import Response
from django.db import transaction
from rest_framework_simplejwt.tokens import RefreshToken
from common.docs import *
from rest_framework.permissions import AllowAny


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
            if not user:
                return Response({'message': 'User not authenticated', 'data': None},
                                status=status.HTTP_401_UNAUTHORIZED)
            serializer = self.serializer_class(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            logging.error(f"Error occurred: {e}")
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
