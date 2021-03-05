from django.db import models


class Thematics(models.Model):
    section_name = models.CharField(max_length=256, verbose_name='Тематика')

    class Meta:
        verbose_name = 'Тематика'
        verbose_name_plural = 'Тематики'

    def __str__(self):
        return self.section_name


class Article(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение', )
    thematic_sections = models.ManyToManyField(Thematics, through='ArticleThematics')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title


class ArticleThematics(models.Model):
    Article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        related_name='article'
    )

    Thematics = models.ForeignKey(
        Thematics,
        on_delete=models.CASCADE,
        related_name='thematics'
    )
    main_thematic = models.BooleanField(default=False)
