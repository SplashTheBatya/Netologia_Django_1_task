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

    # Прекрасный двойной цикл :D
    for list_iter in reader:
        for key in list_iter.keys():
            # Костыль :)
            if key == 'Год':
                list_iter[key] = '<td>' + list_iter[key]
            # Ещё костыль ;)
            elif key == 'Суммарная':
                pass
            elif list_iter[key] == '-':
                list_iter[key] = '<td>' + list_iter[key]
            elif float(list_iter[key]) < 0:
                list_iter[key] = '<td style="background-color: darkgreen">' + list_iter[key]
            elif 1 < float(list_iter[key]) < 2:
                list_iter[key] = '<td style="background-color: #ffa48f">' + list_iter[key]
            elif 2 < float(list_iter[key]) < 5:
                list_iter[key] = '<td style="background-color: #fe6f5e">' + list_iter[key]
            elif float(list_iter[key]) > 5:
                list_iter[key] = '<td style="background-color: red">' + list_iter[key]
            else:
                list_iter[key] = '<td>' + list_iter[key]
        # И наконец-то 1 строчка готова !!!
        data_list.append({
            'Year': list_iter['Год'],
            'Jan': list_iter['Янв'],
            'Feb': list_iter['Фев'],
            'Mar': list_iter['Мар'],
            'Apr': list_iter['Апр'],
            'May': list_iter['Май'],
            'Jun': list_iter['Июн'],
            'Jul': list_iter['Июл'],
            'Aug': list_iter['Авг'],
            'Sep': list_iter['Сен'],
            'Oct': list_iter['Окт'],
            'Nov': list_iter['Ноя'],
            'Dec': list_iter['Дек'],
            'Summary': list_iter['Суммарная'],
        })

    # Ура, солнце зашло, Джанго может отдохнуть
    context = {'years_data': data_list}

    return render(request, template_name,
                  context)
