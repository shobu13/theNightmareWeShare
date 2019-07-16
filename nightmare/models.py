from datetime import timedelta

from django.db import models
from django.utils import timezone
from django.core.exceptions import PermissionDenied
from django.utils.timezone import datetime, utc
from markdownx.models import MarkdownxField


class Nightmare(models.Model):
    name = models.CharField(max_length=150)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    date_creation = models.DateTimeField(default=timezone.now)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return '{} de {}'.format(self.name, self.author)


class NightmarePart(models.Model):
    id = models.AutoField(primary_key=True)
    priority = models.IntegerField()
    nightmare = models.ForeignKey('Nightmare', on_delete=models.CASCADE,
                                  related_name='nightmareparts')
    image = models.ImageField(upload_to='nightmare_part/', blank=True, null=True)
    text = MarkdownxField()

    def __str__(self):
        return 'partie n°{} de {}'.format(self.priority, self.nightmare.name)


class NightmareSurvey(models.Model):
    part = models.OneToOneField('NightmarePart', on_delete=models.CASCADE,
                                related_name='nightmaresurvey')
    duration = models.DurationField(default=timedelta(minutes=10))
    date_creation = models.DateTimeField(default=timezone.now)

    def get_time_left(self):
        """
        Une fonction retournant le temps restant en minute et seconde avant que le questionnaire ne se finisse.
        les 2 champs sont mis a -1 si le questionnaire est finis.
        """
        time_left = self.date_creation + self.duration - timezone.now()
        if (self.date_creation + self.duration) > timezone.now():
            minutes = int(time_left.seconds // 60)
            seconds = time_left.seconds - 60 * int(time_left.seconds // 60)
            return {'minutes': minutes, 'seconds': seconds}
        else:
            return {'minutes': -1, 'seconds': -1}

    def __str__(self):
        return f'questionnaire de {str(self.part)}'

    def get_end_time(self):
        return self.date_creation + self.duration


class NightmareSurveyProposition(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150)
    votes = models.ManyToManyField('auth.User', blank=True, null=True)
    survey = models.ForeignKey('NightmareSurvey', on_delete=models.CASCADE,
                               related_name='nightmaresurveypropositions')

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self.survey.get_end_time() < datetime.now(utc):
            # on empêche la modification des propositons si le temps est écouler.
            raise PermissionDenied('the survey is ended')

    def __str__(self):
        return f'Proposition {self.name} de {str(self.survey)}'
