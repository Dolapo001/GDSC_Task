from django.db import models
from core.models import User
from common.models import BaseModel


class WorkExperience(BaseModel):
    FULL_TIME = 'Full-time'
    PART_TIME = 'Part-time'
    CONTRACT = 'Contract'
    JOB_TYPES = [
        (FULL_TIME, 'Full-time'),
        (PART_TIME, 'Part-time'),
        (CONTRACT, 'Contract'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='work_experiences')
    job_title = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    job_type = models.CharField(choices=JOB_TYPES, max_length=50)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f'{self.job_title} at {self.company_name}'

    def clean(self):
        from django.core.exceptions import ValidationError
        if self.end_date and self.start_date > self.end_date:
            raise ValidationError('End date must be after the start date.')
