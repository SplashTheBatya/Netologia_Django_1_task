from django.views.generic import ListView
from django.shortcuts import render

from articles.models import Article, ArticleThematics


def articles_list(request):
    template = 'articles/news.html'
    print(ArticleThematics.objects.select_related('Article'))
    context = {}

    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    ordering = '-published_at'

    return render(request, template, context)
