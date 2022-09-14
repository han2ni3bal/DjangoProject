# -*- coding: utf-8 -*-

from django.db import models


class CommonTask(models.Model):
  name = models.CharField(max_length=128, blank=True, default="")

  class Meta:
    abstract = True
