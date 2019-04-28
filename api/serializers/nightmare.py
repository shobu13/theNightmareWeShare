from rest_framework import serializers

from core.serializers import UserSerializer
from nightmare.models import Nightmare, NightmarePart, NightmareSurvey, NightmareSurveyProposition


class NightmareSurveyPropositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = NightmareSurveyProposition
        fields = ('id', 'name', 'vote')


class NightmareSurveySerializer(serializers.ModelSerializer):
    nightmaresurveypropositions = NightmareSurveyPropositionSerializer(many=True)

    class Meta:
        model = NightmareSurvey
        fields = ('id', 'duration', 'date_creation', 'nightmaresurveypropositions')


class NightmarePartSerializer(serializers.ModelSerializer):
    nightmaresurvey = NightmareSurveySerializer(many=False)

    class Meta:
        model = NightmarePart
        fields = ('number', 'image', 'text', 'nightmaresurvey')


class NightmareSerializer(serializers.ModelSerializer):
    author = UserSerializer(many=False)

    class Meta:
        model = Nightmare
        fields = ('id', 'name', 'date_creation', 'completed', 'author', 'nightmareparts')


class NightmareDetailSerializer(serializers.ModelSerializer):
    nightmareparts = NightmarePartSerializer(many=True)

    class Meta:
        model = Nightmare
        fields = '__all__'
        depth = 1
