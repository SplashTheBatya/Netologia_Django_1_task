# Generated by Django 3.1.2 on 2021-03-07 12:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_auto_20210305_2055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='thematic_sections',
            field=models.ManyToManyField(related_name='thematics', through='articles.ArticleThematics', to='articles.Thematics'),
        ),
        migrations.AlterField(
            model_name='articlethematics',
            name='Article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='article', to='articles.article'),
        ),
    ]