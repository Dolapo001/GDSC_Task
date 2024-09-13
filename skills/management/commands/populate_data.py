from django.core.management.base import BaseCommand
from skills.models import Skill, Interest


class Command(BaseCommand):
    help = 'Populate database with predefined skills and interests'

    def handle(self, *args, **options):
        predefined_skills = [
            'Python', 'JavaScript', 'Django', 'React', 'Data Science',
            'Java', 'C++', 'Ruby', 'PHP', 'Swift', 'Kotlin', 'Golang', 'Rust'
        ]
        predefined_interests = [
            'Music', 'Art', 'Technology', 'Sports', 'Travel',
            'Cooking', 'Reading', 'Photography', 'Fitness', 'Gaming', 'Writing', 'DIY'
        ]

        # Populate Skills
        for skill_name in predefined_skills:
            skill, created = Skill.objects.get_or_create(name=skill_name)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully created skill: {skill_name}'))
            else:
                self.stdout.write(self.style.WARNING(f'Skill already exists: {skill_name}'))

        # Populate Interests
        for interest_name in predefined_interests:
            interest, created = Interest.objects.get_or_create(name=interest_name)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully created interest: {interest_name}'))
            else:
                self.stdout.write(self.style.WARNING(f'Interest already exists: {interest_name}'))
