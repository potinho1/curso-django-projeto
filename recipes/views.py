from django.shortcuts import render


def home(request):
    return render(request, 'recipes/pages/home.html', context={
        'name': 'POTINHO',
    })


def recipes(request, id):
    return render(request, 'recipes/pages/recipe-view.html', context={
        'name': 'POTINHO',
    })
