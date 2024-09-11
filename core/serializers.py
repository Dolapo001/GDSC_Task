from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import *
from .validators import *


class RegistrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(validators=[validate_email])
    phone = serializers.CharField(validators=[validate_phone])
    password = serializers.CharField(write_only=True, validators=[validate_password_complexity])

    class Meta:
        model = User
        fields = ['name', 'email', 'password', 'phone']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password'],
            phone=validated_data['phone']
        )
        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        # Authenticate user
        user = authenticate(email=email, password=password)
        if not user:
            raise serializers.ValidationError("Invalid credentials")

        data['user'] = user
        return data


class UserProfileSerializer(serializers.ModelSerializer):
    profile_picture = serializers.ImageField(validators=[validate_image], required=False
                                             )
    class Meta:
        model = User
        fields = ['email', 'name', 'phone', 'profile_picture']

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.phone = validated_data.get('phone', instance.phone)
        if 'profile_picture' in validated_data:
            instance.profile_picture = validated_data['profile_picture']
        instance.save()
        return instance
