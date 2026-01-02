# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import InventoryItemForm
from .models import *

# @login_required(login_url="/login/")
# def index(request):
#     context = {'segment': 'index'}
#
#     html_template = loader.get_template('home/index.html')
#     return HttpResponse(html_template.render(context, request))


# Page "home" ou "index" par défaut
@login_required(login_url="/login/")
def item_list(request):
    items = InventoryItem.objects.all()
    return render(request, 'home/index.html', {'items': items})

@login_required(login_url="/login/")
@permission_required('home.InventoryItem', raise_exception=True)
def add_item(request):
    if request.method == 'POST':
        form = InventoryItemForm(request.POST)
        if form.is_valid():
            # form.save() :
            # 1. Sauvegarde équipement
            # 2. Sauvegarde liaisons ManyToMany avec les "sites"
            form.save()
            return redirect('home')
    else:
        form = InventoryItemForm()
        # Forcer un tri alphabétique dans le formulaire
        form.fields['assigned_to'].queryset = Employee.objects.all().order_by('full_name')
        form.fields['site'].queryset = Site.objects.all().order_by('name')

    return render(request, 'home/add_item.html', {'form': form})

@login_required(login_url="/login/")
@permission_required('home.InventoryItem', raise_exception=True)
def edit_item(request, pk):
    item = get_object_or_404(InventoryItem, pk=pk)
    if request.method == 'POST':
        form = InventoryItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = InventoryItemForm(instance=item)
    return render(request, 'home/edit_item.html', {'form': form, 'item': item})

@login_required(login_url="/login/")
@permission_required('home.InventoryItem', raise_exception=True)
def delete_item(request, pk):
    item = get_object_or_404(InventoryItem, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('home')
    return render(request, 'home/delete_item.html', {'item': item})


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))
