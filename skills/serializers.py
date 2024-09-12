from rest_framework import serializers
from .models import *


# Skill Serializers
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


# Interest Serializers
class InterestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interest
        fields = ['id', 'name']


class UserInterestSerializer(serializers.ModelSerializer):
    interest = InterestSerializer(read_only=True)

    class Meta:
        model = UserInterest
        fields = ['id', 'interest']


class AddUserInterestSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInterest
        fields = ['interest']

    def validate_interest(self, value):
        if not Interest.objects.filter(id=value.id).exists():
            raise serializers.ValidationError("Selected interest does not exist.")
        return value
