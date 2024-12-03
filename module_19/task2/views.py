from idlelib.rpc import request_queue

from django.contrib.admin.templatetags.admin_list import pagination
from django.core.paginator import Paginator
from django.shortcuts import render
from .models import *

# Create your views here.


def menu(request):
    return render(request, 'menu.html')


def teams(request):
    Teams = Team.objects.all()
    context1 = {
        'teams': Teams,
    }
    return render(request, 'teams.html', context1)


def players(request):
    list_of_players = Player.objects.all()
    context2 = {'list_of_players': list_of_players}
    return render(request, 'players.html', context2)


def sign_up_by_html(request):
    users = Player.objects.all()
    info = {}
    context = {
        'info': info
    }
    user = None
    context2 = {
        'uZr': user
    }
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        patronymic = request.POST.get('patronymic')
        family = request.POST.get('family')
        city = request.POST.get('city')
        age = int(request.POST.get('age'))
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        if password != repeat_password:
            info.update({'error': 'Пароли не совпадают!'})
            return render(request, 'registration_page.html', context)
        elif age < 18:
            info.update({'error': 'Вы должны быть старше 18!'})
            return render(request, 'registration_page.html', context)
        for user in users:
            if user.family == family and user.first_name == first_name and user.patronymic == patronymic\
                   and user.city == city and user.age == age:
                info.update({'error': 'Пользователь уже существует, обратитесь к администратору!'})
                return render(request, 'registration_page.html', context)
        if password == repeat_password and age >= 18:
            context2.update({'uZr': f'Приветствуем, {first_name}!'})
            Player.objects.create(first_name=first_name, patronymic=patronymic, family=family,
                                  city=city, age=age)
        return render(request, 'registration_page.html', context2)
    return render(request, 'registration_page.html')



def news(request):
    posts = News.objects.all().order_by('-created_at')
    nums = request.GET.get('nums', 3)
    try:
        nums = int(nums)
    except ValueError:
        nums = 3
    paginator = Paginator(posts, nums)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'news.html', {'page_obj': page_obj, 'nums': nums})
