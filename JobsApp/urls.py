from django.urls import path
from JobsApp import views

urlpatterns = [
    path('', views.jobApi),
    path("/<int:id>", views.jobApi),
]