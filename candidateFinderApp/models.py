from django.db import models

# Create your models here.

class Skill(models.Model):
    # SkillId = models.AutoField(primary_key=True)
    SkillName = models.CharField(primary_key=True, max_length=24)

class Candidate(models.Model):
    CandidateId = models.AutoField(primary_key=True)
    CandidateTitle = models.CharField(max_length=100)
    CandidateSkills = models.ManyToManyField(Skill)

class Job(models.Model):
    JobId = models.AutoField(primary_key=True)
    JobTitle = models.CharField(max_length=100)
    JobSkills = models.ManyToManyField(Skill)