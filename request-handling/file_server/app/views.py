import datetime
import os

from django.shortcuts import render
from django.conf import settings


files = os.listdir(settings.FILES_PATH)


def file_list(request, date: datetime = None):
    if date is None:
        context_list = []
        for file_iter in range(len(files)):
            stat_res = os.stat(f'{settings.FILES_PATH}\\{files[file_iter]}')
            context_list.append({'name': files[file_iter],
                                'ctime': datetime.datetime.fromtimestamp(stat_res.st_ctime).date(),
                                 'mtime': datetime.datetime.fromtimestamp(stat_res.st_mtime).date()})
    else:
        context_list = []
        for file_iter in range(len(files)):
            stat_res = os.stat(f'{settings.FILES_PATH}\\{files[file_iter]}')
            ctime = datetime.datetime.fromtimestamp(stat_res.st_ctime).date()
            if ctime == date:
                context_list.append({'name': files[file_iter],
                                     'ctime': ctime,
                                     'mtime': datetime.datetime.fromtimestamp(stat_res.st_mtime).date()})
    return render(request, 'index.html', context={
        'files': context_list,
        'date': date
    })


def file_content(request, name):
    for search_iter in range(len(files)):
        if files[search_iter] == name:
            stat_res = os.stat(f'{settings.FILES_PATH}\\{files[search_iter]}')
            content = ''
            f = open(f'{settings.FILES_PATH}\\{files[search_iter]}')
            for line in f:
                content += f.readline()
            return render(
                request,
                'file_content.html',
                context={'file_name': files[search_iter], 'file_content': content}

    )

