from django.db import models


class App(models.Model):
    heroku_id = models.CharField(max_length=100)
    name = models.CharField(max_length=100)


class Group(models.Model):
    name = models.CharField(max_length=100)
    apps = models.ManyToManyField(App, blank=True)
