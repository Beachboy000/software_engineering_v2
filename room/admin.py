from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin
from .models import Room

@admin.register(Room)
class accountFilter(ImportExportActionModelAdmin):
    list_display = ('id', 'seq', 'date', 'roomID', 'start', 'end', 'purpose')
    list_filter = ('id', 'date', 'roomID')
    list_per_page = 20
# Register your models here.
#admin.site.register(Room)
