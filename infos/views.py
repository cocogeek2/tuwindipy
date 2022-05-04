from infos.models import Info
from infos.serializers import InfoSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
# Create your views here.

@csrf_exempt
def InfoApi(request, idInfo=0):
    if request.method == 'GET':
        info = Info.objects.all()
        Info_serializer=InfoSerializer(info,many=True)
        return JsonResponse(Info_serializer.data,safe=False)
    elif request.method=='POST':
        info_data=JSONParser().parse(request)
        Info_serializer=InfoSerializer(data=info_data)
        if Info_serializer.is_valid():
            Info_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        info_data=JSONParser().parse(request)
        info=Info.objects.get(idInfo=info_data['idInfo'])
        Info_serializer=InfoSerializer(info,data=info_data)
        if Info_serializer.is_valid():
            Info_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        info=Info.objects.get(idInfo=idInfo)
        info.delete()
        return JsonResponse("Deleted Successfully",safe=False)