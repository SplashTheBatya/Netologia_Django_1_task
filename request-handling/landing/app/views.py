from collections import Counter
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render

# Для отладки механизма ab-тестирования используйте эти счетчики
# в качестве хранилища количества показов и количества переходов.
# но помните, что в реальных проектах так не стоит делать
# так как при перезапуске приложения они обнулятся
counter_show = Counter()
counter_click = Counter()


def index(request):
    # Реализуйте логику подсчета количества переходов с лендига по GET параметру from-landing
    url = str(request.META.get('HTTP_REFERER', 'unknown'))
    print(url)
    tags = url.split('=')
    for item in tags:
        for dict_key in settings.REQ_AB_TEST_DICT.keys():
            if item == dict_key:
                counter_click[dict_key] += 1
                print(counter_click[dict_key])
    return render(request, 'index.html')


def landing(request):
    # Реализуйте дополнительное отображение по шаблону app/landing_alternate.html
    # в зависимости от GET параметра ab-test-arg
    # который может принимать значения original и test
    # Так же реализуйте логику подсчета количества показов

    land_val = request.GET.get('from-landing')
    if land_val is None:
        raise Exception('Укажите тип лендинга')

    counter_show[land_val] += 1
    print(counter_show[land_val])
    return render(request, settings.REQ_AB_TEST_DICT[land_val])


def stats(request):
    # Реализуйте логику подсчета отношения количества переходов к количеству показов страницы
    if int(counter_show['test']) == 0 or int(counter_show['original'] == 0):
        return render(request, 'stats.html', context={
            'test_conversion': int(counter_click['test']) / 1,
            'original_conversion': int(counter_click['original']) / 1,
        })
    else:
        return render(request, 'stats.html', context={
            'test_conversion': int(counter_click['test']) / int(counter_show['test']),
            'original_conversion': int(counter_click['original']) / int(counter_show['original']),
        })
