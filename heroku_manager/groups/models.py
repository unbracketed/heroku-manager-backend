from django.db import models
from django.utils.text import slugify


class App(models.Model):
    heroku_id = models.CharField(max_length=100)
    name = models.CharField(max_length=100)


class Group(models.Model):
    name = models.CharField(max_length=100)
    apps = models.ManyToManyField(App, blank=True)
    slug = models.SlugField(unique=True)

    def save(self, **kwargs):
        self.slug = slugify(self.name)
        return super(Group, self).save()
