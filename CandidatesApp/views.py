from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from CandidatesApp.models import Candidate
from CandidatesApp.serializers import CandidateSerializer
from candidateFinderApp.helpers import checkValidSkills
# Create your views here.
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
                candidate_data['CandidateSkills'] = [skill.lower() for skill in candidate_data['CandidateSkills']]
                candidate_serializer = CandidateSerializer(data=candidate_data)
                print(candidate_serializer)
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
                candidate_data['CandidateSkills'] = [skill.lower() for skill in candidate_data['CandidateSkills']]
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