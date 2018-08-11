import os
import sys
import json


sys.path.append('/Users/martin/Documents/projects/homepage/homepage')
os.environ['DJANGO_SETTINGS_MODULE'] = 'homepage.settings'


import django


django.setup()

from homepage.models import Project


with open('data/projects-full.json', 'r') as f:
    data = json.load(f)

for row in data:
    project = Project(project_type=row['username'],
                        title=row['title'],
                        image=row['image'],
                        description=row['description'],
                        live_link=row['live_link'],
                        source_code=row['source_code'],
                        blog_link=row['blog_link'])
    project.save()
