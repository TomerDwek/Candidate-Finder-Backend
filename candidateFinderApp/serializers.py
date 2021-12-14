from rest_framework import serializers
from candidateFinderApp.models import Candidate, Skill, Job

class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = ('CandidateId', 'CandidateTitle', 'CandidateSkills')

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ('SkillName', )

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ('JobId', 'JobTitle', 'JobSkills')
