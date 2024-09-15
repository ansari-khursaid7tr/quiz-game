import os
from django.core.management.base import BaseCommand
from quiz_app.models import Question

class Command(BaseCommand):
    help = 'Load questions from a file'

    def handle(self, *args, **kwargs):
        # Delete all existing questions
        Question.objects.all().delete()

        file_path = os.path.join(os.path.dirname(__file__), 'questions.txt')
        with open(file_path, 'r') as file:
            lines = file.readlines()
            for line in lines:
                text, answer = line.strip().split('|')
                Question.objects.create(text=text, answer=answer)
        self.stdout.write(self.style.SUCCESS('Successfully loaded questions'))
