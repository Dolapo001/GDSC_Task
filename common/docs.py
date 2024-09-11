from drf_spectacular.utils import OpenApiExample, OpenApiResponse, extend_schema
from rest_framework import status


def registration_docs():
    return extend_schema(
        summary="Register a User",
        description=(
            """
            This endpoint allows users to register by providing the necessary details such as
            name, email, password, and phone number.
            """
        ),
        tags=['Authentication'],
        request={
            "application/json": {
                "type": "object",
                "properties": {
                    "name": {"type": "string"},
                    "email": {"type": "string"},
                    "password": {"type": "string"},
                    "phone": {"type": "string"},
                },
                "required": ["name", "email", "password", "phone"],
            }
        },
        responses={
            status.HTTP_201_CREATED: OpenApiResponse(
                description="User registered successfully.",
                response={"application/json"},
                examples=[
                    OpenApiExample(
                        name="Success Response",
                        value={
                            "id": 1,
                            "message": "User registered successfully"
                        }
                    )
                ]
            ),
            status.HTTP_400_BAD_REQUEST: OpenApiResponse(
                description="Invalid data provided.",
                response={"application/json"},
                examples=[
                    OpenApiExample(
                        name="Error Response",
                        value={
                            "errors": {
                                "email": ["This field must be a valid email address."],
                                "password": [
                                    "Password must contain at least one digit.",
                                    "Password must contain at least one letter.",
                                    "Password must contain at least one special character."
                                ]
                            },
                            "data": None
                        }
                    )
                ]
            ),
            status.HTTP_500_INTERNAL_SERVER_ERROR: OpenApiResponse(
                description="Internal Server Error",
                response={"application/json"},
                examples=[
                    OpenApiExample(
                        name="Error Response",
                        value={
                            "message": "Internal Server Error",
                            "data": None
                        }
                    )
                ]
            )
        }
    )


def login_docs():
    return extend_schema(
        summary="Student Login",
        description=(
            """
            This endpoint allows a registered user to log in using their email and password.
            """
        ),
        tags=['Authentication'],
        request={
            "application/json": {
                "type": "object",
                "properties": {
                    "email": {"type": "string"},
                    "password": {"type": "string"},
                },
                "required": ["email", "password"],
            }
        },
        responses={
            status.HTTP_200_OK: OpenApiResponse(
                description="Login successful.",
                response={"application/json"},
                examples=[
                    OpenApiExample(
                        name="Success Response",
                        value={
                            "refresh": "refresh_token_here",
                            "access": "access_token_here"
                        }
                    )
                ]
            ),
            status.HTTP_400_BAD_REQUEST: OpenApiResponse(
                description="Invalid credentials provided.",
                response={"application/json"},
                examples=[
                    OpenApiExample(
                        name="Error Response",
                        value={
                            "email": ["This field must be a valid email address."],
                            "password": ["Incorrect password."]
                        }
                    )
                ]
            ),
            status.HTTP_500_INTERNAL_SERVER_ERROR: OpenApiResponse(
                description="Internal Server Error",
                response={"application/json"},
                examples=[
                    OpenApiExample(
                        name="Error Response",
                        value={
                            "message": "Internal Server Error",
                            "data": None
                        }
                    )
                ]
            )
        }
    )


def user_profile_docs():
    return extend_schema(
        summary="Retrieve User Profile",
        description=(
            """
            This endpoint retrieves the profile of the authenticated user.
            """
        ),
        tags=['User Profile'],
        responses={
            status.HTTP_200_OK: OpenApiResponse(
                description="User profile details.",
                response={"application/json"},
                examples=[
                    OpenApiExample(
                        name="Success Response",
                        value={
                            "email": "user@example.com",
                            "name": "User Name",
                            "phone": "1234567890",
                            "profile_picture": "https://example.com/profile_picture.jpg"
                        }
                    )
                ]
            ),
            status.HTTP_401_UNAUTHORIZED: OpenApiResponse(
                description="Unauthorized access.",
                response={"application/json"},
                examples=[
                    OpenApiExample(
                        name="Error Response",
                        value={
                            "message": "User not authenticated",
                            "data": None
                        }
                    )
                ]
            ),
            status.HTTP_500_INTERNAL_SERVER_ERROR: OpenApiResponse(
                description="Internal Server Error",
                response={"application/json"},
                examples=[
                    OpenApiExample(
                        name="Error Response",
                        value={
                            "message": "Internal Server Error",
                            "data": None
                        }
                    )
                ]
            )
        }
    )
