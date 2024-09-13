from rest_framework import serializers
from .models import Skill, UserSkill, Interest, UserInterest
from core.models import User
# Skill Serializers


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['name']


class UserSkillSerializer(serializers.ModelSerializer):
    skill = SkillSerializer(read_only=True)

    class Meta:
        model = UserSkill
        fields = ['id', 'skill']


class AddUserSkillSerializer(serializers.ModelSerializer):
    skill = serializers.CharField()  # Accept skill name as a string

    class Meta:
        model = UserSkill
        fields = ['skill']

    def validate_skill(self, value):
        # Fetch the skill by its name
        try:
            skill = Skill.objects.get(name=value)
        except Skill.DoesNotExist:
            raise serializers.ValidationError("Selected skill does not exist.")
        return skill

    def create(self, validated_data):
        user = self.context['request'].user
        skill = validated_data['skill']
        return UserSkill.objects.create(user=user, skill=skill)


class UserSearchSerializer(serializers.ModelSerializer):
    skills = UserSkillSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['name', 'skills']


# Interest Serializers
class InterestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interest
        fields = ['name']


class UserInterestSerializer(serializers.ModelSerializer):
    interest = InterestSerializer(read_only=True)

    class Meta:
        model = UserInterest
        fields = ['id', 'interest']


class AddUserInterestSerializer(serializers.ModelSerializer):
    interest = serializers.CharField()

    class Meta:
        model = UserInterest
        fields = ['interest']

    def validate_interest(self, value):
        try:
            interest = Interest.objects.get(name=value)
        except Interest.DoesNotExist:
            raise serializers.ValidationError("Selected interest does not exist.")
        return interest

    def create(self, validated_data):
        user = self.context['request'].user
        interest = validated_data['interest']
        return UserInterest.objects.create(user=user, interest=interest)
