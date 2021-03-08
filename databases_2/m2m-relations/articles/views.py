from django.views.generic import ListView
from django.shortcuts import render

from articles.models import Article, ArticleThematics


def articles_list(request):
    template = 'articles/news.html'
    ordering = '-published_at'
    context = {'object_list': Article.objects.prefetch_related('thematic_sections').order_by(ordering),
               }

    return render(request, template, context)
