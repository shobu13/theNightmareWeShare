from django.contrib import admin
import nested_admin

from nightmare.models import *


class NightmareSurveyPropositionInline(nested_admin.NestedTabularInline):
    model = NightmareSurveyProposition
    extra = 2

    classes = ['collapse']


class NightmareSurveyInline(nested_admin.NestedTabularInline):
    model = NightmareSurvey
    extra = 0

    inlines = [
        NightmareSurveyPropositionInline,
    ]


class NightmarePartInline(nested_admin.NestedTabularInline):
    model = NightmarePart
    extra = 0

    inlines = [
        NightmareSurveyInline,
    ]


class NightmareAdmin(nested_admin.NestedModelAdmin):
    inlines = [
        NightmarePartInline,
    ]


admin.site.register(Nightmare, NightmareAdmin)
