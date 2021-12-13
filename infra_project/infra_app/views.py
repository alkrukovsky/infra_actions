from django.http import HttpResponse


def index(request):
    return HttpResponse('У меня получилось!')


def second_page(request):
    a = 1
    return HttpResponse('А это вторая страница')
