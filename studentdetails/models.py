from django.db import models
import datetime


class ProjectOne(models.Model):
    slack_name = models.CharField(max_length=50, null=True, blank=True)
    current_day = models.DateField(null=True, blank=True)
    track = models.CharField(max_length=250, null=True, blank=True)
    utc_time = models.DateTimeField(null=True, blank=True)
    github_file_url = models.URLField(max_length=300, blank=True, null=True)
    github_repo_url = models.URLField(max_length=200, blank=True, null=True)
    status_code = models.IntegerField(null=200, blank=True)

    def __str__(self):
        return self.slack_name | "HNG task for stage one"

