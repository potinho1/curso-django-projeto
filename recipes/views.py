from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'recipes/home.html', context={
        'name': 'POTINHO',
    })


def contato(request):
    return render(request, 'recipes/contato.html', context={
        'name1': 'pots',
    })


def sobre(request):
    return HttpResponse('sobre')
