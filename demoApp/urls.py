#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.urls import path

from demoApp.views import healthy_check, project_view

app_name = "demoApp"

_healthy_url = [
  path("healthy_check", healthy_check.index, name="index"),

]

_project_url = [
  path("projects/<str:name>", project_view.ProjectsCreateListViews.as_view(), name="demo_project"),
]

urlpatterns = _healthy_url + _project_url
