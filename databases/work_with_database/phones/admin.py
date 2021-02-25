from django.contrib import admin
from phones.models import Phone
# Register your models here.


class PhonesAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    pass


admin.site.register(Phone, PhonesAdmin)
