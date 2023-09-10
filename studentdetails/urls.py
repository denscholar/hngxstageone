from django.urls import path
from . import views

urlpatterns = [
    path("api/", views.ProjectOneAPIView.as_view(), name="project"),
]
