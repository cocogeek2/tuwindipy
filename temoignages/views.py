from temoignages.models import Temoignage
from temoignages.serializers import TemoignageSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
import requests
from django.shortcuts import render

# Create your views here.

@csrf_exempt
def TemoignageApi(request, idTemoignage=0):
    if request.method == 'GET':
        temoignage = Temoignage.objects.all()
        Temoignage_serializer=TemoignageSerializer(temoignage,many=True)
        return JsonResponse(Temoignage_serializer.data,safe=False)
    elif request.method=='POST':
        temoignage_data=JSONParser().parse(request)
        Temoignage_serializer=TemoignageSerializer(data=temoignage_data)
        if Temoignage_serializer.is_valid():
            Temoignage_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        temoignage_data=JSONParser().parse(request)
        temoignage=Temoignage.objects.get(idTemoignage=temoignage_data['idTemoignage'])
        Temoignage_serializer=TemoignageSerializer(temoignage,data=temoignage_data)
        if Temoignage_serializer.is_valid():
            Temoignage_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        temoignage=Temoignage.objects.get(idTemoignage=idTemoignage)
        temoignage.delete()
        return JsonResponse("Deleted Successfully",safe=False)

def temoignages(request):
    #temoignages = requests.get('http://127.0.0.1:8000/temoignage')
    return render(request, 'testimonials.html')