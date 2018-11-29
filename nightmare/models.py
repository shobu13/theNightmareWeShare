from django.db import models
from django.utils.timezone import datetime
from markdownx.models import MarkdownxField


class Nightmare(models.Model):
    name = models.CharField(max_length=150)
    author = models.ForeignKey('User', on_delete=models.CASCADE)
    date_creation = models.DateField(default=datetime.now())


class NightmareSurvey(models.Model):
    pass


class NightmarePart(models.Model):
    nightmare = models.ForeignKey('Nightmare', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='nightmare_part/')
    text = MarkdownxField()
    survey = models.ForeignKey('NightmareSurvey', on_delete=models.CASCADE, blank=True, null=True)
