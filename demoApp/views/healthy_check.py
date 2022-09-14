# -*- coding: UTF-8 -*-
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def index(request):
  response = {"message": "Welcome to Yifan He's demo app"}
  return JsonResponse(response)
