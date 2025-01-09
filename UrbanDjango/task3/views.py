from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.

def platform_view(request):
    return render(request, 'third_task/platform.html')

def games_view(request):
    games = {
        'game1': 'Atomic Heart',
        'game2': 'Cyberpunk 2077',
        'game3': 'Ведьмак 3'
    }
    return render(request, 'third_task/games.html', {'games': games})

def cart_view(request):
    return render(request, 'third_task/cart.html')
