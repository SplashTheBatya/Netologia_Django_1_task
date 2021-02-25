from django.shortcuts import render
from phones.models import Phone


def show_catalog(request):
    template = 'catalog.html'

    sort_tag = request.GET.get('sort')
    if sort_tag is None:
        sort_tag = 'name'
    if sort_tag == 'ascending':
        context = {'Phones': Phone.objects.all().order_by('price')}
    elif sort_tag == 'descending':
        context = {'Phones': Phone.objects.all().order_by('-price')}
    else:
        context = {'Phones': Phone.objects.all().order_by('name')}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {'Phone': Phone.objects.get(slug=slug)}
    return render(request, template, context)
