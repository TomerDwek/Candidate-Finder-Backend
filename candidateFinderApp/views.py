from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from candidateFinderApp.models import Job, Candidate, Skill
from candidateFinderApp.serializers import CandidateSerializer, JobSerializer, SkillSerializer
# Create your views here.

@csrf_exempt
def jobApi(request, id=0):
    match request.method:
        case 'GET':
            try:
                jobs = Job.objects.all()
                job_serializer = JobSerializer(jobs, many=True)
                return JsonResponse(job_serializer.data, safe=False)
            except: 
                return JsonResponse('Failed to fetch jobs!')
        case 'POST':
            try:
                job_data = JSONParser().parse(request)
                if checkValidSkills(job_data['JobSkills']) == False:
                    return JsonResponse('Failed to Add Job! Not all of the requested skills are in the skills list', safe=False)
                job_serializer = JobSerializer(data=job_data)
                if (job_serializer.is_valid()):
                    job_serializer.save()
                    return JsonResponse('Job Added Succesfully!', safe=False)
            except:
                return JsonResponse('Failed to Add Job!', safe=False)
        case 'PUT':
            try:
                if id == 0:
                    return JsonResponse('Must specify job ID in order to update it!', safe=False) 
                job_data = JSONParser().parse(request)
                if checkValidSkills(job_data['JobSkills']) == False:
                    return JsonResponse('Failed to Update Job! Not all of the requested skills are in the skills list', safe=False)
                job = Job.objects.get(JobId=id)
                job_serializer = JobSerializer(job, data=job_data)
                if job_serializer.is_valid():
                    job_serializer.save()
                    return JsonResponse('Job Updated Succesfully!', safe=False) 
            except:
                return JsonResponse('Failed to Update Job!', safe=False)
        case 'DELETE':
            try:
                if id == 0:
                    return JsonResponse('Must specify job ID in order to delete it!', safe=False) 
                job = Job.objects.get(JobId=id)
                job.delete()
                return JsonResponse('Job Deleted Succesfully!', safe=False)
            except:
                return JsonResponse('Failed to Delete job!', safe=False)

@csrf_exempt
def skillApi(request, name=''):
    match request.method:
        case 'GET':
            try:
                skills = Skill.objects.all()
                skill_serializer = SkillSerializer(skills, many=True)
                return JsonResponse(skill_serializer.data, safe=False)
            except:
                return JsonResponse('Failed to fetch skills!', safe=False)
        case 'POST':
            try:
                skill_data = JSONParser().parse(request)
                skill_data['SkillName'] = skill_data['SkillName'].lower()
                if Skill.objects.filter(SkillName = skill_data['SkillName']).exists():
                    return JsonResponse("Skill already existing!", safe=False)
                skill_serializer = SkillSerializer(data=skill_data)
                if (skill_serializer.is_valid()):
                    skill_serializer.save()
                    return JsonResponse('Skill Added Succesfully!', safe=False)
            except:
                return JsonResponse('Failed to Add Skill!', safe=False)
        case 'PUT':
            return JsonResponse("Can't update a skill, you can remove or create new one", safe=False)
            # try:
            #     if name == '':
            #         return JsonResponse('Must specify skill name in order to update it!', safe=False)
            #     skill_data = JSONParser().parse(request)
            #     skill = Skill.objects.get(SkillName=str(name))
            #     skill_serializer = SkillSerializer(skill, data=skill_data)
            #     if skill_serializer.is_valid():
            #         skill_serializer.save()
            #         return JsonResponse('Skill Updated Succesfully!', safe=False)
            # except: 
            #     return JsonResponse('Failed to Update Skill!', safe=False)
        case 'DELETE':
            try:
                if name == '':
                    return JsonResponse('Must specify skill name in order to delete it!', safe=False)
                skill = Skill.objects.get(SkillName=str(name).lower())
                print(skill)
                skill.delete()
                return JsonResponse('Skill Deleted Succesfully!', safe=False)
            except:
                return JsonResponse('Failed to Delete skill!', safe=False)

@csrf_exempt
def candidateApi(request, id=0):
    match request.method:
        case 'GET':
            try:
                candidates = Candidate.objects.all()
                candidate_serializer = CandidateSerializer(candidates, many=True)
                return JsonResponse(candidate_serializer.data, safe=False)
            except:
                return JsonResponse('Failed to ferch candidates!', safe=False)
        case 'POST':
            try:
                candidate_data = JSONParser().parse(request)
                if checkValidSkills(candidate_data['CandidateSkills']) == False:
                    return JsonResponse('Failed to Add Candidate! Not all of the requested skills are in the skills list', safe=False)
                candidate_serializer = CandidateSerializer(data=candidate_data)
                if (candidate_serializer.is_valid()):
                    candidate_serializer.save()
                    return JsonResponse('Candidate Added Succesfully!', safe=False)
            except:
                return JsonResponse('Failed to Add Candidate!', safe=False)
        case 'PUT':
            try:
                if id == 0:
                    return JsonResponse('Must specify candidate ID in order to update it!', safe=False) 
                candidate_data = JSONParser().parse(request)
                if checkValidSkills(candidate_data['CandidateSkills']) == False:
                    return JsonResponse('Failed to Update Candidate! Not all of the requested skills are in the skills list', safe=False)
                candidate = Candidate.objects.get(CandidateId=id)
                candidate_serializer = CandidateSerializer(candidate, data=candidate_data)
                if candidate_serializer.is_valid():
                    candidate_serializer.save()
                    return JsonResponse('Candidate Updated Succesfully!', safe=False) 
            except:
                return JsonResponse('Failed to Update Candidate!', safe=False)
        case 'DELETE':
            try:
                if id == 0:
                    return JsonResponse('Must specify candidate ID in order to delete it!', safe=False) 
                candidate = Candidate.objects.get(CandidateId=id)
                candidate.delete()
                return JsonResponse('Candidate Deleted Succesfully', safe=False)
            except:
                return JsonResponse('Failed to Delete candidate!', safe=False)

def checkValidSkills(skills):
    for skill in skills:
        if not Skill.objects.filter(SkillName = skill).exists():
                    return False
    return True

@csrf_exempt
def findCandidate(request, job_id=0):
    try:
        if job_id == 0:
            return JsonResponse('Must enter job id to search the best candidate!', safe=False)
        job = Job.objects.get(JobId=job_id)
        candidates = Candidate.objects.filter(CandidateTitle=job.JobTitle)
        if (len(candidates) == 0):
            return JsonResponse('There is no suitable candidate for this position!', safe=False)
        job_skills = [skill.SkillName for skill in list(job.JobSkills.all())]
        best_candidate = candidates.first()
        max_len = 0
        for candidate in candidates:
            candidate_skills = [skill.SkillName for skill in list(candidate.CandidateSkills.all())]
            if len(set(candidate_skills).intersection(job_skills)) > max_len:
                best_candidate = candidate
                max_len = len(set(candidate_skills).intersection(job_skills))
        best_candidate_serialize = CandidateSerializer(best_candidate)
        return JsonResponse(best_candidate_serialize.data, safe=False)
    except:
        return JsonResponse('Failed to find a suitable candidate', safe=False)
