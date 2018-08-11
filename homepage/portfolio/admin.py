from django.contrib import admin
from .models import ProjectType, Project, Technology

# Register your models here.
admin.site.register(ProjectType)
admin.site.register(Project)
admin.site.register(Technology)
