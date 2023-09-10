from rest_framework import serializers
from .models import ProjectOne


class ProjectOneSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectOne
        fields = (
            "slack_name",
            "current_day",
            "track",
            "utc_time",
            "github_file_url",
            "github_repo_url",
            "status_code",
        )
