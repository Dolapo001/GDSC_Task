# Models
from common.models import BaseModel
from django.db import models
from core.models import User


class Skill(BaseModel):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Interest(BaseModel):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class UserSkill(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='skills')
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.name} - {self.skill.name}'


class UserInterest(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='interests')
    interest = models.ForeignKey(Interest, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.name} - {self.interest.name}'
