import logging
from django.db import transaction
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *
from django.db.models import Q
from core.models import User
from common.docs import *


class SkillListView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = SkillSerializer

    @skill_list_docs()
    def get(self, request):
        try:
            skills = Skill.objects.all()
            serializer = self.serializer_class(skills, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            logging.error(f"Error occurred: {e}")
            return Response({'message': f'Internal Server Error: {str(e)}', 'data': None},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class AddUserSkillView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSkillSerializer

    @transaction.atomic()
    @add_user_skills_docs()
    def post(self, request):
        try:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                serializer.save(user=request.user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logging.error(f"Error occurred: {e}")
            return Response({'message': f'Internal Server Error: {str(e)}', 'data': None},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class UserSkillListView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSkillSerializer

    @user_skill_list_docs()
    def get(self, request):
        try:
            user_skills = UserSkill.objects.filter(user=request.user)
            serializer = self.serializer_class(user_skills, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            logging.error(f"Error occurred: {e}")
            return Response({'message': f'Internal Server Error: {str(e)}', 'data': None},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class UserSkillDeleteView(APIView):
    permission_classes = [IsAuthenticated]

    @transaction.atomic()
    @user_skill_delete_docs()
    def delete(self, request, pk):
        try:
            user_skill = get_object_or_404(UserSkill, pk=pk, user=request.user)
            user_skill.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            logging.error(f"Error occurred: {e}")
            return Response({'message': f'Internal Server Error: {str(e)}', 'data': None},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class UserSearchView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSkillSerializer

    @user_search_docs()
    def get(self, request):
        try:
            skills_query = request.query_params.get('skills')
            job_type_query = request.query_params.get('job_type')
            users = User.objects.all()

            if skills_query:
                users = users.filter(skills__skill__name__icontains=skills_query)

            if job_type_query:
                users = users.filter(work_experiences__job_type=job_type_query)

            users = users.distinct()

            if not users.exists():
                return Response({"detail": "No users found matching the criteria."}, status=status.HTTP_404_NOT_FOUND)
            serializer = self.serializer_class(users, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            logging.error(f"Error occurred: {e}")
            return Response({'message': f'Internal Server Error: {str(e)}', 'data': None},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

