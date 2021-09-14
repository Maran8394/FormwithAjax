from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from . models import *

class Personal_DetailsAdmin(admin.ModelAdmin):
    list_display = ('f_name','l_name',)

admin.site.register(Personal_Details,Personal_DetailsAdmin)