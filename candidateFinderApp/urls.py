from django.urls import path
from candidateFinderApp import views

urlpatterns = [
    path("", views.findCandidate)
]