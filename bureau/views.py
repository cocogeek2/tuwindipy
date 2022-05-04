from bureau.models import Bureau
from bureau.serializers import BureauSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
# Create your views here.

@csrf_exempt
def BureauApi(request, idBureau=0):
    if request.method == 'GET':
        bureau = Bureau.objects.all()
        Bureau_serializer=BureauSerializer(bureau,many=True)
        return JsonResponse(Bureau_serializer.data,safe=False)
    elif request.method=='POST':
        article_data=JSONParser().parse(request)
        Bureau_serializer=BureauSerializer(data=article_data)
        if Bureau_serializer.is_valid():
            Bureau_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        article_data=JSONParser().parse(request)
        bureau=Bureau.objects.get(idBureau=article_data['idBureau'])
        Bureau_serializer=BureauSerializer(bureau,data=article_data)
        if Bureau_serializer.is_valid():
            Bureau_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        bureau=Bureau.objects.get(idBureau=idBureau)
        bureau.delete()
        return JsonResponse("Deleted Successfully",safe=False)