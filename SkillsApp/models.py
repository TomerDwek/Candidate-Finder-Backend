from django.db import models

# Create your models here.

class Skill(models.Model):
    SkillName = models.CharField(primary_key=True, max_length=24)