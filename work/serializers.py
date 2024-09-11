from rest_framework import serializers
from .models import WorkExperience


class WorkExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkExperience
        fields = ['id', 'job_title', 'company_name', 'location', 'job_type', 'start_date', 'end_date', 'description']

    def validate(self, data):
        if data.get('end_date') and data['start_date'] > data['end_date']:
            raise serializers.ValidationError("End date must be after start date.")
        return data


class WorkExperienceDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkExperience
        fields = ['id', 'job_title', 'company_name', 'location', 'job_type', 'start_date', 'end_date', 'description']


class WorkExperienceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkExperience
        fields = ['id', 'job_title', 'company_name']
