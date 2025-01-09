from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.

def menu_view(request):
    return render(request, 'fourth_task/menu.html')

def games_view(request):

    context = {
        'games': ['Atomic Heart', 'Cyberpunk 2077', 'Ведьмак 3']
    }
    return render(request, 'fourth_task/games.html', context)

def cart_view(request):
    return render(request, 'fourth_task/cart.html')