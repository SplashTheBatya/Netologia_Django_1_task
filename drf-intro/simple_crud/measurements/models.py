from django.db import models


class Timing(models.Model):
    created_at = models.DateTimeField(
        null=False,
        auto_now_add=True
    ).auto_now
    updated_at = models.DateTimeField(
        null=False,
        auto_now=True
    ).auto_now_add

    class Meta:
        abstract = True


class Project(Timing):
    """Объект на котором проводят измерения."""

    name = models.TextField(null=False)
    latitude = models.FloatField(null=False)
    longitude = models.FloatField(null=False)


class Measurement(Timing):
    """Измерение температуры на объекте."""

    value = models.FloatField(null=False)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    screen = models.ImageField(null=True)
