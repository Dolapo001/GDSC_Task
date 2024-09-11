import logging
from django.db import transaction
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from .models import WorkExperience
from .serializers import WorkExperienceListSerializer, WorkExperienceDetailSerializer, WorkExperienceSerializer
from common.docs import *


class WorkExperienceListView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = WorkExperienceListSerializer

    @work_experience_list_docs()
    def get(self, request):
        try:
            work_experiences = WorkExperience.objects.filter(user=request.user)
            if not work_experiences.exists():
                return Response(
                    {'message': 'No work experiences found for this user.', 'data': None},
                    status=status.HTTP_404_NOT_FOUND
                )
            serializer = self.serializer_class(work_experiences, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            logging.error(f"Error occurred: {e}")
            return Response({'message': f'Internal Server Error: {str(e)}', 'data': None},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class WorkExperienceCreateView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = WorkExperienceSerializer

    @transaction.atomic()
    @create_work_experience_docs()
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


class WorkExperienceDetailView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = WorkExperienceDetailSerializer

    @work_experience_detail_docs()
    def get(self, request, pk):
        try:
            work_experience = get_object_or_404(WorkExperience, pk=pk, user=request.user)
            serializer = self.serializer_class(work_experience)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            logging.error(f"Error occurred: {e}")
            return Response({'message': f'Internal Server Error: {str(e)}', 'data': None},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class WorkExperienceEditView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = WorkExperienceSerializer

    @transaction.atomic()
    @work_experience_edit_docs()
    def put(self, request, pk):
        try:
            work_experience = get_object_or_404(WorkExperience, pk=pk, user=request.user)
            serializer = self.serializer_class(work_experience, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logging.error(f"Error occurred: {e}")
            return Response({'message': f'Internal Server Error: {str(e)}', 'data': None},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class WorkExperienceDeleteView(APIView):
    permission_classes = [IsAuthenticated]

    @transaction.atomic()
    @work_experience_delete_docs()
    def delete(self, request, pk):
        try:
            work_experience = get_object_or_404(WorkExperience, pk=pk, user=request.user)
            work_experience.delete()
            return Response({'message': 'Work experience deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            logging.error(f"Error occurred: {e}")
            return Response({'message': f'Internal Server Error: {str(e)}', 'data': None},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
