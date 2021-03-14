from django.db import models


class Project(models.Model):
    """Объект на котором проводят измерения."""

    name = models.TextField(null=False)
    latitude = models.FloatField(null=False)
    longitude = models.FloatField(null=False)
    created_at = models.DateTimeField(
        null=False,
        auto_now_add=True
    ).auto_now
    updated_at = models.DateTimeField(
        null=False,
        auto_now=True
    ).auto_now_add


class Measurement(models.Model):
    """Измерение температуры на объекте."""

    value = models.FloatField(null=False)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    created_at = models.DateTimeField(
        auto_now_add=True,
        null=False
    ).auto_now
    updated_at = models.DateTimeField(
        auto_now=True,
        null=False
    ).auto_now_add
