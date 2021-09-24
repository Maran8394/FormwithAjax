from typing import ClassVar
from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from . models import Contact_Us

# class AuthorAdmin(admin.ModelAdmin):
#     change_form_template = "change_admin.html"
admin.site.register(Contact_Us)