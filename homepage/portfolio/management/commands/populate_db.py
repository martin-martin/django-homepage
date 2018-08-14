import os
import json
from homepage.settings import BASE_DIR
from django.core.management.base import BaseCommand
from django.core.files import File
from portfolio.models import Project, Technology, ProjectType

class Command(BaseCommand):
    args = ''
    help = 'Inserts the project data into the Django default database.'


    # TODO: build some SQL queries that check whether the entries already
    #       exist, and only create them if they don't

    def _enter_projects(self):
        with open('portfolio/data/projects-full.json', 'r') as f:
            data = json.load(f)

        for row in data:
            project = Project(title=row['title'],
                                description=row['description'],
                                live_link=row['live_link'],
                                source_code=row['source_code'],
                                blog_link=row['blog_link'])
            project.save()

            image_name = row['image']
            abs_path = os.path.join(BASE_DIR,
                                "portfolio/data/screenshots/" + image_name)

            with open(abs_path, 'rb') as f:
                django_file = File(f)
                project.image.save(image_name, django_file)


    # NOTE: ATTENTION!!! Currently there is no check whether or not the
    #       following entries already exist in the database, and for some
    #       reason the script adds them to the database as double-entries
    #       attempts to change this remained fruitless so far, because
    #       it requires manually assigning the primary_key to the model
    #       class (as done for Projects), but attempting this for the
    #       other classes too results in problems with the ManyToMany
    #       relationship, so I left it at this for now.
    #
    #       I suggest to keep the below code commented-out after the first
    #       time db population, and add further tech and types manually.

    #def _enter_technologies(self):
    #    with open('portfolio/data/tech.json', 'r') as f:
    #        data = json.load(f)

    #    for item in data:
    #        tech = Technology(name=item)
    #        tech.save()

    #def _enter_project_types(self):
    #    with open('portfolio/data/project_types.json', 'r') as f:
    #        data = json.load(f)

    #    for item in data:
    #        p_type = ProjectType(name=item['type'], priority=item['priority'])
    #        p_type.save()

    # might not be necessary, maybe all _functions() get run anyways (?)
    def handle(self, *args, **options):
        self._enter_projects()
      # self._enter_project_types()
      # self._enter_technologies()

# HELPFUL RESOURCES:
# https://eli.thegreenplace.net/2014/02/15/programmatically-populating-a-django-database
# https://stackoverflow.com/questions/1308386/programmatically-saving-image-to-django-imagefield
