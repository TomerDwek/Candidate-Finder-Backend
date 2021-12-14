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
                return JsonResponse(skill_serializer.data, safe=False)
            except:
                return JsonResponse('Failed to fetch skills!', safe=False)
        case 'POST':
            try:
                print(request)
                skill_data = JSONParser().parse(request)
                if len(skill_data['SkillName']) == 0:
                    return JsonResponse('Skill Name Cannot Be Empty!', safe=False)
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