from rest_framework import serializers

from nightmare.models import Nightmare, NightmarePart, NightmareSurvey, NightmareSurveyProposition


class NightmareSurveyPropositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = NightmareSurveyProposition
        fields = ('id', 'name', 'vote')


class NightmareSurveySerializer(serializers.ModelSerializer):
    nightmaresurveypropositions = NightmareSurveyPropositionSerializer(many=True)

    class Meta:
        model = NightmareSurvey
        fields = ('id', 'duration', 'date_creation', 'completed', 'nightmaresurveypropositions')


class NightmarePartSerializer(serializers.ModelSerializer):
    nightmarsurvey = NightmareSurveySerializer(many=True)

    class Meta:
        model = NightmarePart
        fields = ('id', 'number', 'image', 'text', 'nightmarsurvey')


class NightmareSerializer(serializers.ModelSerializer):
    nightmareparts = NightmarePartSerializer(many=True)

    class Meta:
        model = Nightmare
        fields = ('id', 'name', 'date_creation', 'completed', 'author', 'nightmareparts')
