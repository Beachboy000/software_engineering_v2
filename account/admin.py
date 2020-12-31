from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin
from .models import Account

@admin.register(Account)
class accountFilter(ImportExportActionModelAdmin):
    #list_display = [field.name for field in Account._meta.fields] #display all account content

    list_display = ('id','userName',)
    list_filter = ('id',)
    list_per_page = 10

    #ordering = ('-mod_date',)
    #list_filter = ('userName')
# Register your models here.
#admin.site.register(Account)

