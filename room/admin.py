from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin
from .models import Room

@admin.register(Room)
class accountFilter(ImportExportActionModelAdmin):
    list_display = ('id',)
    list_filter = ('id',)
    list_per_page = 20
# Register your models here.
#admin.site.register(Room)
