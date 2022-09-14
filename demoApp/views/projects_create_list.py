# -*- coding: UTF-8 -*-
from django.conf import settings
from django.http import JsonResponse
from demoApp.models import DemoJob
from kubernetes import client, config
from kubernetes.client.rest import ApiException


def process_post_project(request, body, **kwargs):
  try:
    # check body from request
    body = check_and_get_body_in_v2_projects(body)
  except Exception as e:
    return JsonResponse({"error": True, "message": e.args[0]}, status=400)
  if request:
    operator = request.z_args.get("usr", request.user)
  else:
    # simulate request params
    request_org_id = kwargs.get('org_id', None)
  is_public = body.get("is_public", False)
  # to do some opreation, like add to mysql or send to k8s
  demoObject = DemoJob.objects.filter(job_name=body["job_name"], delete_time=None)
  is_success, api_response = create_object(demoObject)
  ....
  if not is_success:
    return api_response
  else:
    ...
    return JsonResponse({"data": 200})


def list_projects(request):
  ...
