from SkillsApp.models import Skill
from rest_framework.parsers import JSONParser

def checkValidSkills(skills):
    for skill in skills:
        if not Skill.objects.filter(SkillName = skill.lower()).exists():
                    return False
    return True