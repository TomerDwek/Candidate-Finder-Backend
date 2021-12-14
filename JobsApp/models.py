from django.db import models
from SkillsApp.models import Skill

# Create your models here.
class Job(models.Model):
    JobId = models.AutoField(primary_key=True)
    JobTitle = models.CharField(max_length=100)
    JobSkills = models.ManyToManyField(Skill)
