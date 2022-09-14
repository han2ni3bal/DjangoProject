# -*- coding: UTF-8 -*-
from rest_framework.authentication import BaseAuthentication
from rest_framework.generics import ListCreateAPIView
from demoApp.views import projects_create_list


class ProjectsCreateListViews(ListCreateAPIView):
  authentication_classes = [BaseAuthentication]

  def create(self, request, *args, **kwargs):
    body = request.data
    return projects_create_list.process_post_project(request, body)

  def list(self, request, *args, **kwargs):
    return projects_create_list.list_projects(request)
