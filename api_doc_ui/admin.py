from django.contrib import admin

# Register your models here.
from api_doc_ui import models


class DemoModelAdmin(admin.ModelAdmin):
    list_display = ['asdf', 'ttt']


admin.site.register(models.DemoModel)
