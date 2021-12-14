from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser

from SkillsApp.models import Skill
from SkillsApp.serializers import SkillSerializer

# Create your views here.
@csrf_exempt
def skillApi(request, name=''):
    match request.method:
        case 'GET':
            try:
                skills = Skill.objects.all()
                skill_serializer = SkillSerializer(skills, many=True)
                return JsonResponse(skill_serializer.data, safe=False, status=200)
            except:
                return JsonResponse('Failed to fetch skills!', safe=False, status=404)
        case 'POST':
            try:
                print(request)
                skill_data = JSONParser().parse(request)
                if len(skill_data['SkillName']) == 0:
                    return JsonResponse('Skill Name Cannot Be Empty!', safe=False, status=400)
                skill_data['SkillName'] = skill_data['SkillName'].lower()
                if Skill.objects.filter(SkillName = skill_data['SkillName']).exists():
                    return JsonResponse("Skill already existing!", safe=False, status=400)
                skill_serializer = SkillSerializer(data=skill_data)
                if (skill_serializer.is_valid()):
                    skill_serializer.save()
                    return JsonResponse(skill_serializer.data, safe=False, status=201)
            except:
                return JsonResponse('Failed to Add Skill!', safe=False, status=404)
        case 'PUT':
            return JsonResponse("Can't update a skill, you can remove or create new one", safe=False, status=400)
        case 'DELETE':
            try:
                if name == '':
                    return JsonResponse('Must specify skill name in order to delete it!', safe=False, status=400)
                skill = Skill.objects.get(SkillName=str(name).lower())
                print(skill)
                skill.delete()
                return JsonResponse('Skill Deleted Succesfully!', safe=False, status=200)
            except:
                return JsonResponse('Failed to Delete skill!', safe=False, status=404)