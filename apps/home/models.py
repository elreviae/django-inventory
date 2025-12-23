# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
# from django.contrib.auth.models import User

# Create your models here.
class Site(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Nom du site")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Site"
        verbose_name_plural = "Sites"

class Employee(models.Model):
    full_name = models.CharField(max_length=200, verbose_name="Nom complet de l'employé")
    # Un employé peut appartenir à plusieurs sites
    sites = models.ManyToManyField(Site, verbose_name="Sites d'affectation")

    def __str__(self):
        # Affiche le nom et ses sites pour aider l'admin
        # sites_list = ", ".join([site.name for site in self.sites.all()])
        # return f"{self.full_name} ({sites_list})"
        return f"{self.full_name}"

    class Meta:
        verbose_name = "Employé"
        verbose_name_plural = "Employés"
        ordering = ['full_name']

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
    # null=True permet à la base d'accepter du vide
    # blank=True permet au formulaire de laisser le champ vide
    assigned_to = models.ForeignKey(
        Employee,
        on_delete=models.SET_NULL,  # Si l'employé est supprimé, l'objet reste mais devient libre
        blank=True,
        null=True,
        verbose_name="Attribué à"
    )
    site = models.ForeignKey(
        Site,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name="Site"
    )
    purchase_date = models.DateField(blank=True, null=True, verbose_name="Date d'achat")
    notes = models.TextField(blank=True, null=True, verbose_name="Notes")

    def __str__(self):
        return f"{self.site}  {self.brand} {self.model} ({self.serial_number})"

    class Meta:
        verbose_name = "Élément d'inventaire"
        verbose_name_plural = "Éléments d'inventaire"
        ordering = ['brand', 'model', 'site']
