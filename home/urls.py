# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("pos_page/", views.pos_page, name="pos_page"),
]
