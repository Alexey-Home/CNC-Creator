from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


class PicturesAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "pictures")
    search_fields = ("title",)

    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.pictures.url}' width=50>")

    get_html_photo.short_description = "Миниатюра"




class ProgramAdmin(admin.ModelAdmin):
    list_display = ("id_user", "name", "program")



admin.site.register(Program, ProgramAdmin)
admin.site.register(Pictures, PicturesAdmin)