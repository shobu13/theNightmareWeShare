from django.shortcuts import render


def read(request, nightmare_id):
    return render(request, 'nightmare/read.html')
