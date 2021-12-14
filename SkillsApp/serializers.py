from rest_framework import serializers
from SkillsApp.models import Skill

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ('SkillName', )