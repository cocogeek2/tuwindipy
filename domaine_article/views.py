from domaine_article.models import Domaine
from domaine_article.serializers import DomaineSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
# Create your views here.

@csrf_exempt
def DomaineApi(request, idDomaine=0):
    if request.method == 'GET':
        domaine = Domaine.objects.all()
        Domaine_serializer=DomaineSerializer(domaine,many=True)
        return JsonResponse(Domaine_serializer.data,safe=False)
    elif request.method=='POST':
        domaine_data=JSONParser().parse(request)
        Domaine_serializer=DomaineSerializer(data=domaine_data)
        if Domaine_serializer.is_valid():
            Domaine_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        domaine_data=JSONParser().parse(request)
        domaine=Domaine.objects.get(idDomaine=domaine_data['idDomaine'])
        Domaine_serializer=DomaineSerializer(domaine,data=domaine_data)
        if Domaine_serializer.is_valid():
            Domaine_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        domaine=Domaine.objects.get(idDomaine=idDomaine)
        domaine.delete()
        return JsonResponse("Deleted Successfully",safe=False)