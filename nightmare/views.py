from django.shortcuts import render

from nightmare.models import Nightmare


def home(request):
    nightmares = Nightmare.objects.all()
    return render(request, 'nightmare/home.html', locals())


def read(request, nightmare_id):
    nightmare = Nightmare.objects.get(id=nightmare_id)
    return render(request, 'nightmare/read.html', locals())
