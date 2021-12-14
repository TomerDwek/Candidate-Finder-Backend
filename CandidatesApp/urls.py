from django.urls import path
from CandidatesApp import views

urlpatterns = [
    path('', views.candidateApi),
    path("/<int:id>", views.candidateApi),
]