# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
# from django.contrib.auth.models import User

# Create your models here.
class EquipmentType(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Type d'équipement")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Type d'équipement"
        verbose_name_plural = "Types d'équipement"
        ordering = ['name']

class Brand(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Marque")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Marque"
        verbose_name_plural = "Marques"
        ordering = ['name']

class InventoryItem(models.Model):
    type = models.ForeignKey(EquipmentType, on_delete=models.PROTECT, verbose_name="Type d'équipement")
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, verbose_name="Marque")
    model = models.CharField(max_length=100, verbose_name="Modèle")
    serial_number = models.CharField(max_length=100, unique=True, verbose_name="Numéro de série")
    assigned_to = models.CharField(max_length=200, blank=True, null=True, verbose_name="Attribué à")
    purchase_date = models.DateField(blank=True, null=True, verbose_name="Date d'achat")
    notes = models.TextField(blank=True, null=True, verbose_name="Notes")

    def __str__(self):
        return f"{self.brand} {self.model} ({self.serial_number})"

    class Meta:
        verbose_name = "Élément d'inventaire"
        verbose_name_plural = "Éléments d'inventaire"
        ordering = ['brand', 'model']
