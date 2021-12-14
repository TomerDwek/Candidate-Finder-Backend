from django.urls import path
from SkillsApp import views

urlpatterns = [
    path('', views.skillApi),
    path("/<str:name>", views.skillApi)
]