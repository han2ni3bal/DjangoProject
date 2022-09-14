import time

import requests
from django.conf import settings
from django.core.management.base import BaseCommand
# FalconData is used to send the heart beat for monitoring
import FalconData

import logging


class Command(BaseCommand):
  help = "Detect runserver heartbeat"

  def __init__(self):
    super(Command, self).__init__()
    self.sleep_interval = 9
    self.should_stop = False
    # endpoint is the server endpoint
    self.url = endpoint + "/demo/healthy_check"

  def handle(self, *args, **options):
    while self.url and (not self.should_stop):
      try:
        ret = requests.get(self.url)
        if ret.status_code != 200:
          logging.error("Detect heartbeat failed, request status_code {}, "
                       "ret {}".format(ret.status_code, ret.content))
          self.run_heartbeat(value=1)
        else:
          logging.debug("Detect heartbeat success, request status_code {}, "
                       "ret {}".format(ret.status_code, ret.content))
          self.run_heartbeat(value=0)
      except Exception as e:
        logging.error("Detect heartbeat failed: {}".format(str(e)))
        self.run_heartbeat(value=1)
      time.sleep(self.sleep_interval)
    logging.info("Detect runserver heartbeat shutdown, url: {}".format(self.url))

  def run_heartbeat(self, value):
    self.upload_to_falcon(value)

  def upload_to_falcon(self, value):
    if not settings.ENABLE_FALCON_UPLOAD:
      self.should_stop = True
      return
    metric = f"xxx"
    data = FalconData(metric=metric, value=value, tags="service=runserver_heartbeat,type=heartbeat")
    data.upload()
