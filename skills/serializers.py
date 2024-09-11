from .models import *
from rest_framework import serializers


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['id', 'name']


class UserSkillSerializer(serializers.ModelSerializer):
    skill = SkillSerializer(read_only=True)

    class Meta:
        model = UserSkill
        fields = ['id', 'skill']


class AddUserSkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSkill
        fields = ['skill']

    def validate_skill(self, value):
        if not Skill.objects.filter(id=value.id).exists():
            raise serializers.ValidationError("Selected skill does not exist.")
        return value
