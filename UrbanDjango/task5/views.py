from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegister

users = ['Kirill', 'Nikita', 'Kate', 'Anna', 'Nina']

def sign_up_by_html(request):
    info = {}

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = int(request.POST.get('age'))

        if username not in users and password == repeat_password and int(age) >= 18:
            users.append(username)
            return HttpResponse(f'Регистрация прошла успешно! Привет, {username}')

        elif username in users:
            info['error'] = HttpResponse('Этот логин уже занят', status=400, reason='repeated login')
            return HttpResponse('Этот логин уже занят', status=400, reason='repeated login')

        elif password != repeat_password:
            info['error'] = HttpResponse('Пароли не совпадают', status=400, reason='non-identical passwords')
            return HttpResponse('Пароли не совпадают', status=400, reason='non-identical passwords')

        elif int(age) < 18:
            info['error'] = HttpResponse(f'Регистрация разрешена с 18ти лет. Будем рады видеть вас через {18-int(age)} лет', status=400, reason='insufficient age')
            return HttpResponse(f'Регистрация разрешена с 18ти лет. Будем рады видеть вас через {18-int(age)} лет', status=400, reason='insufficient age')

    context = {'info':info}
    return render(request, 'fifth_task/registration_page.html', context)


def sign_up_by_django(request):
    info = {}

    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

        if username not in users and password == repeat_password and int(age) >= 18:
            users.append(username)
            return HttpResponse(f'Регистрация прошла успешно! Привет, {username}')

        elif username in users:
            info['error'] = HttpResponse('Этот логин уже занят', status=400, reason='repeated login')
            return HttpResponse('Этот логин уже занят', status=400, reason='repeated login')

        elif password != repeat_password:
            info['error'] = HttpResponse('Пароли не совпадают', status=400, reason='non-identical passwords')
            return HttpResponse('Пароли не совпадают', status=400, reason='non-identical passwords')

        elif int(age) < 18:
            info['error'] = HttpResponse(f'Регистрация разрешена с 18ти лет. Будем рады видеть вас через {18-int(age)} лет', status=400, reason='insufficient age')
            return HttpResponse(f'Регистрация разрешена с 18ти лет. Будем рады видеть вас через {18-int(age)} лет', status=400, reason='insufficient age')

    else:
        form = UserRegister()
        context = {'info': info, 'form': form}
        return render(request, 'fifth_task/registration_page.html', context)


