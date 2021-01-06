from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin
from .models import Seq

@admin.register(Seq)
class accountFilter(ImportExportActionModelAdmin):
    list_display = ('id', 'userName', 'user_num', )
    list_filter = ('id', 'user_num',)
    list_per_page = 20
# Register your models here.
#admin.site.register(Room)
