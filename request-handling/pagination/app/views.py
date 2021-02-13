from csv import DictReader
from urllib import parse


from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse

from django.conf import settings


def index(request):
    return redirect(reverse(bus_stations))


def bus_stations(request):
    current_page = int(request.GET.get('page', 1))

    with open(settings.BUS_STATION_CSV, encoding='cp1251') as csvfile:
        reader = list(DictReader(csvfile))
        paginator = Paginator(reader, settings.REQ_POSTS_PER_PAGE, 2)

    page = paginator.get_page(current_page)
    print(paginator.num_pages)
    data_list = []
    for page_iter in range(len(page) - 1):
        data_list.append({'Name': page[page_iter]['Name'], 'Street': page[page_iter]['Street'],
                          'District': page[page_iter]['District']})

    if page.has_next() is True:
        next_page_url = reverse('bus_stations') + '?' + parse.urlencode({'page': page.next_page_number()})
    else:
        next_page_url = reverse('bus_stations') + '?' + parse.urlencode({'page': 1})

    if page.has_previous() is True:
        prev_page_url = reverse('bus_stations') + '?' + parse.urlencode({'page': page.previous_page_number()})
    else:
        prev_page_url = reverse('bus_stations') + '?' + parse.urlencode({'page': 1})

    return render(request, 'index.html', context={
        'bus_stations': data_list,
        'current_page': current_page,
        'prev_page_url': prev_page_url,
        'next_page_url': next_page_url,
    })
