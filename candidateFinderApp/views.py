from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse

from CandidatesApp.models import Candidate
from JobsApp.models import Job
from CandidatesApp.serializers import CandidateSerializer
# Create your views here.

@csrf_exempt
def findCandidate(request, job_id=0):
    try:
        if job_id == 0:
            return JsonResponse('Must enter job id to search the best candidate!', safe=False, status=400)
        job = Job.objects.get(JobId=job_id)
        candidates = Candidate.objects.filter(CandidateTitle=job.JobTitle)
        if (len(candidates) == 0):
            return JsonResponse('There is no suitable candidate for this position!', safe=False, status=400)
        job_skills = [skill.SkillName for skill in list(job.JobSkills.all())]
        best_candidate = candidates.first()
        max_len = 0
        for candidate in candidates:
            candidate_skills = [skill.SkillName for skill in list(candidate.CandidateSkills.all())]
            if len(set(candidate_skills).intersection(job_skills)) > max_len:
                best_candidate = candidate
                max_len = len(set(candidate_skills).intersection(job_skills))
        best_candidate_serialize = CandidateSerializer(best_candidate)
        return JsonResponse(best_candidate_serialize.data, safe=False, status=200)
    except:
        return JsonResponse('Failed to find a suitable candidate', safe=False, status=404)
