from django.contrib import admin
from .models import * 


class BrotherAdmin(admin.ModelAdmin):

    list_display = ['name', 'age']
    search_fields = ['name']    


admin.site.register(Brother, BrotherAdmin)

admin.site.site_header = "MEPKIN ABBEY ADMIN"



