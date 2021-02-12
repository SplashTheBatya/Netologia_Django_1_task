from django.urls import path, register_converter

from app.views import *


class DateConverter:
    regex = '[0-9]{4}-[0-9]{2}-[0-9]{2}'

    def to_python(self, value):
        return datetime.datetime.strptime(value, '%Y-%m-%d').date()

    def to_url(self, value):
        return value.strftime('%Y-%m-%d')


register_converter(DateConverter, 'date')

urlpatterns = [
    path('', file_list, name='file_list'),
    path('<date:date>/', file_list, name='file_list'),
    path('file_content/<str:name>', file_content, name='file_content'),
]
