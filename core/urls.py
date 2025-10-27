# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from django.urls import path, include  # add this

admin.site.site_header = "Gestion d'Inventaire - Administration"
admin.site.site_title = "Inventaire Admin"
admin.site.index_title = "Bienvenue dans l'administration de l'inventaire"

urlpatterns = [
    path('config/', admin.site.urls),          # Django admin route
    path("", include("apps.authentication.urls")), # Auth routes - login / register

    # ADD NEW Routes HERE
    # Leave `Home.Urls` as last the last line
    path("", include("apps.home.urls"))
]
