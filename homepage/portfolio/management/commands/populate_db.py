import json
from django.core.management.base import BaseCommand
from portfolio.models import Project, Technology, ProjectType

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

    def _enter_technologies(self):
        with open('portfolio/data/tech.json', 'r') as f:
            data = json.load(f)

        for item in data:
            tech = Technology(name=item)
            tech.save()

    def _enter_project_types(self):
        with open('portfolio/data/project_types.json', 'r') as f:
            data = json.load(f)

        for item in data:
            p_type = ProjectType(name=item['type'], priority=item['priority'])
            p_type.save()

    def handle(self, *args, **options):
        self._enter_project_types()
        self._enter_technologies()
        self._enter_projects()

# https://eli.thegreenplace.net/2014/02/15/programmatically-populating-a-django-database
