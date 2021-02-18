import csv

from django.shortcuts import render


def inflation_view(request):
    template_name = 'inflation.html'
    # чтение csv-файла

    csv.register_dialect('my_dialect', delimiter=';')
    with open('inflation_russia.csv', encoding='UTF-8') as csvfile:
        reader = list(csv.DictReader(csvfile, dialect='my_dialect'))
    for list_iter in range(len(reader) - 1):
        for dict_reader in reader[list_iter]:
            if reader[list_iter][dict_reader] == '':
                reader[list_iter][dict_reader] = '-'

    data_list = []

    for list_iter in reader:
        data_list.append({
            'Год': list_iter['Год'],
            'Янв': list_iter['Янв'],
            'Фев': list_iter['Фев'],
            'Мар': list_iter['Мар'],
            'Апр': list_iter['Апр'],
            'Май': list_iter['Май'],
            'Июн': list_iter['Июн'],
            'Июл': list_iter['Июл'],
            'Авг': list_iter['Авг'],
            'Сен': list_iter['Сен'],
            'Окт': list_iter['Окт'],
            'Ноя': list_iter['Ноя'],
            'Дек': list_iter['Дек'],
            'Суммарная': list_iter['Суммарная'],
        })
    print(data_list)
    context = {'years_data': data_list}

    return render(request, template_name,
                  context)
