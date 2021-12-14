from rest_framework import serializers
from CandidatesApp.models import Candidate

class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = ('CandidateId', 'CandidateTitle', 'CandidateSkills')