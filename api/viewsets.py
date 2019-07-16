from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, status
from rest_framework import permissions
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework.settings import api_settings

from api.serializers.nightmare import NightmareSerializer, NightmareDetailSerializer, NightmareSurveySerializer
from nightmare.models import Nightmare, NightmareSurvey


class MultiSerializerViewSet(viewsets.GenericViewSet):
    """
    MultiSerializerViewSet est une class custom permettant l'usage de plusieurs serializer
    en fonction de l'action.
    Elle permet aussi de sélectionner les permissions à accorder en fonction de l'action.
    """
    serializers = {
        'default': None,
    }

    permission_classes = {
        'default': api_settings.DEFAULT_PERMISSION_CLASSES
    }

    def get_serializer_class(self):
        return self.serializers.get(self.action,
                                    self.serializers['default'])

    def get_permissions(self):
        permission_list = self.permission_classes.get(self.action,
                                                      self.permission_classes['default'])
        return [permission() for permission in permission_list]


class NightmareViewset(MultiSerializerViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin,
                       mixins.DestroyModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin):
    queryset = Nightmare.objects.all()
    permission_classes = {
        'default': (permissions.IsAuthenticatedOrReadOnly,),
    }
    serializers = {
        'default': NightmareDetailSerializer,
        'list': NightmareSerializer
    }


class NightmareSurveyViewset(MultiSerializerViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin,
                             mixins.DestroyModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin):
    queryset = NightmareSurvey.objects.all()
    permission_classes = {
        'default': (permissions.IsAuthenticatedOrReadOnly,),
    }
    serializers = {
        'default': NightmareSurveySerializer,
    }

    depth = 1
