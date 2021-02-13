import csv

from django.shortcuts import render


def inflation_view(request):
    template_name = 'inflation.html'
    # чтение csv-файла и заполнение контекста

    csv.register_dialect('my_dialect', delimiter=';')
    with open('inflation_russia.csv', encoding='UTF-8') as csvfile:
        reader = list(csv.DictReader(csvfile, dialect='my_dialect'))
    for list_iter in range(len(reader) - 1):
        for dict_reader in reader[list_iter]:
            if reader[list_iter][dict_reader] == '':
                reader[list_iter][dict_reader] = '-'

    data_list = []
    for list_iter in range(len(reader)):
        data_list.append({
            'Year': reader[list_iter]['Год'],
            'Jan': reader[list_iter]['Янв'],
            'Feb': reader[list_iter]['Фев'],
            'Mar': reader[list_iter]['Мар'],
            'Apr': reader[list_iter]['Апр'],
            'May': reader[list_iter]['Май'],
            'Jun': reader[list_iter]['Июн'],
            'Jul': reader[list_iter]['Июл'],
            'Aug': reader[list_iter]['Авг'],
            'Sep': reader[list_iter]['Сен'],
            'Oct': reader[list_iter]['Окт'],
            'Nov': reader[list_iter]['Ноя'],
            'Dec': reader[list_iter]['Дек'],
            'Summary': reader[list_iter]['Суммарная'],
        })
    context = {'years_data': data_list}

    return render(request, template_name,
                  context)
