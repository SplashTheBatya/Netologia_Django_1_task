from django.db import models
from django.utils.text import slugify
from PIL import Image


class Phone(models.Model):
    name = models.TextField(max_length=255)
    price = models.FloatField()
    image = models.ImageField(upload_to='phones')
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField(max_length=255, unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Phone, self).save(*args, **kwargs)
