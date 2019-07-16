from django.contrib import admin
import nested_admin

from nightmare.models import *


class NightmareSurveyPropositionInline(admin.TabularInline):
    model = NightmareSurveyProposition
    extra = 0
    filter_horizontal = ('votes',)

    classes = ['collapse']


class NightmareSurveyAdmin(admin.ModelAdmin):
    inlines = [
        NightmareSurveyPropositionInline,
    ]


class NightmarePartInline(admin.TabularInline):
    model = NightmarePart
    extra = 0


class NightmareAdmin(admin.ModelAdmin):
    inlines = [
        NightmarePartInline,
    ]


admin.site.register(Nightmare, NightmareAdmin)
admin.site.register(NightmareSurvey, NightmareSurveyAdmin)
