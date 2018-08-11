import json
from django.core.management.base import BaseCommand
from portfolio.models import Project

class Command(BaseCommand):
    args = ''
    help = 'Inserts the project data into the Django default database.'

    def _enter_projects(self):
        with open('portfolio/data/projects-full.json', 'r') as f:
            data = json.load(f)

        for row in data:
            project = Project(title=row['title'],
                                image=row['image'],
                                description=row['description'],
                                live_link=row['live_link'],
                                source_code=row['source_code'],
                                blog_link=row['blog_link'])
            project.save()

    def handle(self, *args, **options):
        self._enter_projects()

# https://eli.thegreenplace.net/2014/02/15/programmatically-populating-a-django-database
