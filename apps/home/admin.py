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

@admin.register(InventoryItem)
class InventoryItemAdmin(admin.ModelAdmin):
    # Les colonnes qui seront affichées dans la liste
    list_display = ('get_full_name', 'type', 'brand', 'model', 'serial_number')
    # Permet de cliquer sur ces éléments pour éditer
    list_display_links = ('get_full_name', 'model')
    # Ajoute des filtres sur le côté droit
    list_filter = ('type', 'brand', 'site')
    # Ajoute une barre de recherche
    search_fields = ('model', 'serial_number', 'assigned_to__full_name')

    # Fonction personnalisée pour afficher le nom de l'employé
    def get_full_name(self, obj):
        if obj.assigned_to:
            return obj.assigned_to.full_name
        return "Non attribué"

    # Nom de la colonne dans l'interface admin
    get_full_name.short_description = 'Employé'
