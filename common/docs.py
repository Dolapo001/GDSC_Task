from drf_spectacular.utils import OpenApiExample, OpenApiResponse, extend_schema, OpenApiParameter
from rest_framework import status
from skills.serializers import *


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


def work_experience_list_docs():
    return extend_schema(
        summary="List Work Experiences",
        description=(
            """
            This endpoint retrieves a list of work experiences for the authenticated user.
            If no work experiences are found, a `404 Not Found` response is returned.
            """
        ),
        tags=['Work Experience'],
        responses={
            status.HTTP_200_OK: OpenApiResponse(
                description="List of work experiences retrieved successfully.",
                response={"application/json"},
                examples=[
                    OpenApiExample(
                        name="Success Response",
                        value=[
                            {
                                "id": 1,
                                "job_title": "Software Engineer",
                                "company_name": "Tech Corp"
                            },
                            {
                                "id": 2,
                                "job_title": "Data Scientist",
                                "company_name": "Data Inc"
                            }
                        ]
                    )
                ]
            ),
            status.HTTP_404_NOT_FOUND: OpenApiResponse(
                description="No work experiences found for this user.",
                response={"application/json"},
                examples=[
                    OpenApiExample(
                        name="Error Response",
                        value={
                            "message": "No work experiences found for this user.",
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


def create_work_experience_docs():
    return extend_schema(
        summary="Create Work Experience",
        description=(
            """
            This endpoint allows the authenticated user to create a new work experience.
            """
        ),
        tags=['Work Experience'],
        request={
            "application/json": {
                "type": "object",
                "properties": {
                    "job_title": {"type": "string"},
                    "company_name": {"type": "string"},
                    "location": {"type": "string"},
                    "job_type": {"type": "string"},
                    "start_date": {"type": "string", "format": "date"},
                    "end_date": {"type": "string", "format": "date"},
                    "description": {"type": "string"}
                },
                "required": ["job_title", "company_name", "start_date"]
            }
        },
        responses={
            status.HTTP_201_CREATED: OpenApiResponse(
                description="Work experience created successfully.",
                response={"application/json"},
                examples=[
                    OpenApiExample(
                        name="Success Response",
                        value={
                            "id": 1,
                            "job_title": "Software Engineer",
                            "company_name": "Tech Corp",
                            "location": "New York",
                            "job_type": "Full-time",
                            "start_date": "2023-01-01",
                            "end_date": "2024-01-01",
                            "description": "Worked on developing web applications."
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
                            "job_title": ["This field is required."],
                            "start_date": ["This field is required."]
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


def work_experience_detail_docs():
    return extend_schema(
        summary="Retrieve Work Experience",
        description=(
            """
            This endpoint retrieves a specific work experience by its ID for the authenticated user.
            """
        ),
        tags=['Work Experience'],
        responses={
            status.HTTP_200_OK: OpenApiResponse(
                description="Work experience details retrieved successfully.",
                response={"application/json"},
                examples=[
                    OpenApiExample(
                        name="Success Response",
                        value={
                            "id": 1,
                            "job_title": "Software Engineer",
                            "company_name": "Tech Corp",
                            "location": "New York",
                            "job_type": "Full-time",
                            "start_date": "2023-01-01",
                            "end_date": "2024-01-01",
                            "description": "Worked on developing web applications."
                        }
                    )
                ]
            ),
            status.HTTP_404_NOT_FOUND: OpenApiResponse(
                description="Work experience not found.",
                response={"application/json"},
                examples=[
                    OpenApiExample(
                        name="Error Response",
                        value={
                            "message": "Work experience not found.",
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


def work_experience_edit_docs():
    return extend_schema(
        summary="Update Work Experience",
        description=(
            """
            This endpoint allows the authenticated user to update a specific work experience.
            """
        ),
        tags=['Work Experience'],
        request={
            "application/json": {
                "type": "object",
                "properties": {
                    "job_title": {"type": "string"},
                    "company_name": {"type": "string"},
                    "location": {"type": "string"},
                    "job_type": {"type": "string"},
                    "start_date": {"type": "string", "format": "date"},
                    "end_date": {"type": "string", "format": "date"},
                    "description": {"type": "string"}
                },
                "required": []  # Fields are optional for partial updates
            }
        },
        responses={
            status.HTTP_200_OK: OpenApiResponse(
                description="Work experience updated successfully.",
                response={"application/json"},
                examples=[
                    OpenApiExample(
                        name="Success Response",
                        value={
                            "id": 1,
                            "job_title": "Senior Software Engineer",
                            "company_name": "Tech Corp",
                            "location": "San Francisco",
                            "job_type": "Full-time",
                            "start_date": "2023-01-01",
                            "end_date": "2024-01-01",
                            "description": "Promoted to senior position."
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
                            "start_date": ["This field is required."]
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


def work_experience_delete_docs():
    return extend_schema(
        summary="Delete Work Experience",
        description=(
            """
            This endpoint allows the authenticated user to delete a specific work experience.
            """
        ),
        tags=['Work Experience'],
        responses={
            status.HTTP_204_NO_CONTENT: OpenApiResponse(
                description="Work experience deleted successfully.",
                response={"application/json"},
                examples=[
                    OpenApiExample(
                        name="Success Response",
                        value={
                            "message": "Work experience deleted successfully."
                        }
                    )
                ]
            ),
            status.HTTP_404_NOT_FOUND: OpenApiResponse(
                description="Work experience not found.",
                response={"application/json"},
                examples=[
                    OpenApiExample(
                        name="Error Response",
                        value={
                            "message": "Work experience not found.",
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


def skill_list_docs():
    return extend_schema(
        summary="List Skills",
        description="Retrieve a list of all available skills.",
        tags=['Skills'],
        responses={
            status.HTTP_200_OK: OpenApiResponse(
                description="A list of skills.",
                response=SkillSerializer(many=True),
                examples=[
                    OpenApiExample(
                        name="Success Response",
                        value=[
                            {"id": 1, "name": "Python"},
                            {"id": 2, "name": "Django"}
                        ]
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


def add_user_skills_docs():
    return extend_schema(
        summary="Add User Skill",
        description="Add a skill to the authenticated user's profile.",
        tags=['Skills'],
        request=UserSkillSerializer,
        responses={
            status.HTTP_201_CREATED: OpenApiResponse(
                description="Skill added successfully.",
                response=UserSkillSerializer,
                examples=[
                    OpenApiExample(
                        name="Success Response",
                        value={
                            "id": 1,
                            "skill": {"id": 2, "name": "Django"}
                        }
                    )
                ]
            ),
            status.HTTP_400_BAD_REQUEST: OpenApiResponse(
                description="Validation error.",
                response={"application/json"},
                examples=[
                    OpenApiExample(
                        name="Error Response",
                        value={
                            "non_field_errors": ["Invalid data."]
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


def user_skill_list_docs():
    return extend_schema(
        summary="List User Skills",
        description="Retrieve a list of all skills associated with the authenticated user.",
        tags=['Skills'],
        responses={
            status.HTTP_200_OK: OpenApiResponse(
                description="A list of the user's skills.",
                response=UserSkillSerializer(many=True),
                examples=[
                    OpenApiExample(
                        name="Success Response",
                        value=[
                            {"id": 1, "skill": {"id": 2, "name": "Django"}}
                        ]
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


def user_skill_delete_docs():
    return extend_schema(
        summary="Delete User Skill",
        description="Remove a skill from the authenticated user's profile.",
        tags=['Skills'],
        responses={
            status.HTTP_204_NO_CONTENT: OpenApiResponse(
                description="Skill deleted successfully.",
                response={"application/json"},
                examples=[
                    OpenApiExample(
                        name="Success Response",
                        value={
                            "message": "Skill deleted successfully."
                        }
                    )
                ]
            ),
            status.HTTP_404_NOT_FOUND: OpenApiResponse(
                description="Skill not found.",
                response={"application/json"},
                examples=[
                    OpenApiExample(
                        name="Error Response",
                        value={
                            "message": "Skill not found.",
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


def user_search_docs():
    return extend_schema(
        summary="Search Users",
        description="Search for users based on skills and job type.",
        tags=['Users'],
        parameters=[
            OpenApiParameter(name='skills', description='Filter users by skill name.', required=False, type=str),
            OpenApiParameter(name='job_type', description='Filter users by job type.', required=False, type=str)
        ],
        responses={
            status.HTTP_200_OK: OpenApiResponse(
                description="A list of users matching the search criteria.",
                response=UserSkillSerializer(many=True),
                examples=[
                    OpenApiExample(
                        name="Success Response",
                        value=[
                            {"id": 1, "skill": {"id": 2, "name": "Django"}}
                        ]
                    )
                ]
            ),
            status.HTTP_404_NOT_FOUND: OpenApiResponse(
                description="No users found matching the criteria.",
                response={"application/json"},
                examples=[
                    OpenApiExample(
                        name="Error Response",
                        value={
                            "detail": "No users found matching the criteria."
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
