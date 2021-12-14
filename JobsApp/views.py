from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from JobsApp.models import Job
from JobsApp.serializers import JobSerializer
from candidateFinderApp.helpers import checkValidSkills

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
                job_data['JobSkills'] = [skill.lower() for skill in job_data['JobSkills']]
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
                job_data['JobSkills'] = [skill.lower() for skill in job_data['JobSkills']]
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