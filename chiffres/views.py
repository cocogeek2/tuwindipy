from chiffres.models import Chiffre
from chiffres.serializers import ChiffreSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
# Create your views here.

@csrf_exempt
def ChiffreApi(request, idChiffre=0):
    if request.method == 'GET':
        chiffre = Chiffre.objects.all()
        Chiffre_serializer=ChiffreSerializer(chiffre,many=True)
        return JsonResponse(Chiffre_serializer.data,safe=False)
    elif request.method=='POST':
        chiffre_data=JSONParser().parse(request)
        Chiffre_serializer=ChiffreSerializer(data=chiffre_data)
        if Chiffre_serializer.is_valid():
            Chiffre_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        chiffre_data=JSONParser().parse(request)
        chiffre=Chiffre.objects.get(idChiffre=chiffre_data['idChiffre'])
        Chiffre_serializer=ChiffreSerializer(chiffre,data=chiffre_data)
        if Chiffre_serializer.is_valid():
            Chiffre_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        chiffre=Chiffre.objects.get(idChiffre=idChiffre)
        chiffre.delete()
        return JsonResponse("Deleted Successfully",safe=False)