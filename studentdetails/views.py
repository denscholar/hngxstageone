from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProjectOneSerializer
from .models import ProjectOne
import datetime


class ProjectOneAPIView(APIView):
    def get(self, request, *args, **kwargs):
        # extra the query parameter
        slack_name = request.GET.get("slack_name", "")
        track = request.GET.get("track", "")

        slack_name = slack_name.lower().replace(" ", "_")

        # calculate trhe current day and UTC time
        current_day = datetime.date.today().strftime("%A")
        utc_time = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")

        # Create an instance of the model with the calculated data

        data = {
            "slack_name": slack_name,
            "current_day": current_day,
            "utc_time": utc_time,
            "track": track,
            "github_file_url": "https://github.com/denscholar/hngxstageone/blob/main/studentdetails/views.py",
            "github_repo_url": "https://github.com/denscholar/hngxstageone",
            "status_code": 200,
        }

        # create the data
        data_instance = ProjectOne(**data)

        serializer = ProjectOneSerializer(instance=data_instance)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
