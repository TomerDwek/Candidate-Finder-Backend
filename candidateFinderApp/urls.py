from django.urls import path
from candidateFinderApp import views

urlpatterns = [
    path('jobs', views.jobApi),
    path("jobs/<int:id>", views.jobApi),
    path('skills', views.skillApi),
    path("skills/<str:name>", views.skillApi),
    path('candidates', views.candidateApi),
    path("candidates/<int:id>", views.candidateApi),
    path("match/<int:job_id>", views.findCandidate)
]