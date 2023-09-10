from django.urls import path
from . import views

urlpatterns = [
    path("", views.ProjectOneAPIView.as_view(), name="project"),
]
