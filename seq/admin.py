from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin
from .models import Seq

@admin.register(Seq)
class accountFilter(ImportExportActionModelAdmin):
    list_display = ('id', 'userName', 'seq', 'user_run', )
    list_filter = ('id', 'user_run',)
    list_per_page = 20
# Register your models here.
#admin.site.register(Room)
