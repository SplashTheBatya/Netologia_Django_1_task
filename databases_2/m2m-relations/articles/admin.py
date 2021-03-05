from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Thematics, ArticleThematics


class ArticleThematicsInlineFormset(BaseInlineFormSet):
    def clean(self):
        counter = 0
        for form in self.forms:
            if form.cleaned_data.get('main_thematic', False):
                counter += 1

        if counter > 1:
            raise ValidationError('Выберите только 1 основную тематику')
        elif counter < 1:
            raise ValidationError('Выберите хотя-бы 1 основную тематику')

        return super().clean()


class ArticleThematicsInline(admin.TabularInline):
    model = ArticleThematics
    formset = ArticleThematicsInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ArticleThematicsInline]


@admin.register(Thematics)
class ThematicsAdmin(admin.ModelAdmin):
    pass
