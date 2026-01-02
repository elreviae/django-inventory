# -*- encoding: utf-8 -*-

from django import forms
from .models import *

class InventoryItemForm(forms.ModelForm):

    class Meta:
        model = InventoryItem
        fields = '__all__'
        widgets = {
            'type': forms.Select(attrs={'class': 'form-select'}),
            'brand': forms.Select(attrs={'class': 'form-select'}),
            'model': forms.TextInput(attrs={'class': 'form-control'}),
            'serial_number': forms.TextInput(attrs={'class': 'form-control'}),
            'assigned_to': forms.Select(attrs={'class': 'form-select'}),
            # 'site': forms.Select(attrs={'class': 'form-select'}),
            'site': forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),
            'purchase_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Supprime la ligne vide '---------' pour les cases à cocher
        self.fields['site'].queryset = Site.objects.all()
        self.fields['site'].empty_label = None

