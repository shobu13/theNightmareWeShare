import math

from django.db import models
from django.utils import timezone
from markdownx.models import MarkdownxField


class Nightmare(models.Model):
    name = models.CharField(max_length=150)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    date_creation = models.DateTimeField(default=timezone.now())
    completed = models.BooleanField(default=False)

    def __str__(self):
        return '{} de {}'.format(self.name, self.author)


class NightmarePart(models.Model):
    number = models.IntegerField()
    nightmare = models.ForeignKey('Nightmare', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='nightmare_part/', blank=True, null=True)
    text = MarkdownxField()

    def __str__(self):
        return 'n°{} de {}'.format(self.number, self.nightmare.name)


class NightmareSurvey(models.Model):
    part = models.ForeignKey('NightmarePart', on_delete=models.CASCADE)
    duration = models.DurationField()
    date_creation = models.DateTimeField(default=timezone.now())
    completed = models.BooleanField(default=False)

    def get_time_left(self):
        return int(round((self.date_creation + self.duration - timezone.now()).total_seconds() / 60, 0))
    # TODO faire une crontask qui vérifie régulièrement les tâches non complétée.


class NightmareSurveyProposition(models.Model):
    name = models.CharField(max_length=150)
    vote = models.IntegerField(default=0)
    survey = models.ForeignKey('NightmareSurvey', on_delete=models.CASCADE)
