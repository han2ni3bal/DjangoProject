from django.db import models
from .common_task import CommonTask
# Create your models here.


class DemoJob(CommonTask):
  # For resource owner and quota
  # For running the script
  job_name = models.CharField(max_length=128)

  def __str__(self):
    return "{}-{}".format(self.org_id, self.job_name)

  @classmethod
  def create(cls, job_name):
    job = cls()
    job.job_name = job_name
    job.save()
    return job
