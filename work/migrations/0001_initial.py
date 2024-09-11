# Generated by Django 5.1.1 on 2024-09-11 22:09

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkExperience',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('job_title', models.CharField(max_length=100)),
                ('company_name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('job_type', models.CharField(choices=[('Full-time', 'Full-time'), ('Part-time', 'Part-time'), ('Contract', 'Contract')], max_length=50)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
                ('description', models.TextField(blank=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='work_experiences', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
