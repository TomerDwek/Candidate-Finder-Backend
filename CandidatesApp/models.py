from django.db import models

from SkillsApp.models import Skill
# Create your models here.

class Candidate(models.Model):
    CandidateId = models.AutoField(primary_key=True)
    CandidateTitle = models.CharField(max_length=100)
    CandidateSkills = models.ManyToManyField(Skill)