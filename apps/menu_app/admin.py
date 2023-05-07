from django.contrib import admin
from django import forms
from .models import Menu

class MenuAdmin(admin.ModelAdmin):
    list_display = ('uri',)
    fields = (
        'name',
        'root',
        'parent',
        'parent_uri',
        'uri',
    )

# Register your models here.
admin.site.register(Menu, MenuAdmin)