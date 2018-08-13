from django.db import models

# Create your models here.

class ProjectType(models.Model):
    name = models.CharField(max_length=100)
    priority = models.IntegerField(default=5)  # what's my range, what's default?

    def __str__(self):
        return self.name


class Technology(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Project(models.Model):
    # project_id = models.IntegerField(primary_key=True, default=0)
    title = models.CharField(primary_key=True, max_length=100)
    project_type = models.ForeignKey(ProjectType,
                                        # allow having no ProjectType association
                                        models.SET_NULL,
                                        blank=True, null=True)
    technologies = models.ManyToManyField(Technology, blank=True)
    image = models.ImageField(upload_to='images',
                                blank=True, null=True)
    description = models.CharField(max_length=1000, blank=True)  # maybe TextField()
    live_link = models.URLField(blank=True, null=True)
    source_code = models.URLField(blank=True, null=True)
    blog_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title
