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
    project_type = models.ForeignKey(ProjectType,
                                        # allow having no ProjectType association
                                        models.SET_NULL,
                                        blank=True, null=True)
    technologies = models.ManyToManyField(Technology)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='folder/url',
                                blank=True, null=True)
    description = models.CharField(max_length=1000)  # maybe TextField()
    live_link = models.URLField()
    source_code = models.URLField()
    blog_link = models.URLField()

    def __str__(self):
        return self.title
