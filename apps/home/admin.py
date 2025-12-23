# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Site)
class SiteAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

admin.site.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


admin.site.register(EquipmentType)
class EquipmentTypeAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

admin.site.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

admin.site.register(InventoryItem)
class InventoryItemAdmin(admin.ModelAdmin):
    list_display = ['type', 'brand', 'model', 'serial_number', 'assigned_to', 'purchase_date']
    list_filter = ['type', 'brand']
    search_fields = ['model', 'serial_number', 'assigned_to']