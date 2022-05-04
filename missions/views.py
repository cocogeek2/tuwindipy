from missions.models import Mission
from missions.serializers import MissionSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
# Create your views here.

@csrf_exempt
def MissionApi(request, idMission=0):
    if request.method == 'GET':
        mission = Mission.objects.all()
        Mission_serializer=MissionSerializer(mission,many=True)
        return JsonResponse(Mission_serializer.data,safe=False)
    elif request.method=='POST':
        mission_data=JSONParser().parse(request)
        Mission_serializer=MissionSerializer(data=mission_data)
        if Mission_serializer.is_valid():
            Mission_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        mission_data=JSONParser().parse(request)
        mission=Mission.objects.get(idMission=mission_data['idMission'])
        Mission_serializer=MissionSerializer(mission,data=mission_data)
        if Mission_serializer.is_valid():
            Mission_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        mission=Mission.objects.get(idMission=idMission)
        mission.delete()
        return JsonResponse("Deleted Successfully",safe=False)