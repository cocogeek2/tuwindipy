from social_network.models import SocialNetwork
from social_network.serializers import SocialNetworkSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
# Create your views here.

@csrf_exempt
def SocialNetworkApi(request, idSocialNetwork=0):
    if request.method == 'GET':
        social_network = SocialNetwork.objects.all()
        SocialNetwork_serializer=SocialNetworkSerializer(social_network,many=True)
        return JsonResponse(SocialNetwork_serializer.data,safe=False)
    elif request.method=='POST':
        social_network_data=JSONParser().parse(request)
        SocialNetwork_serializer=SocialNetworkSerializer(data=social_network_data)
        if SocialNetwork_serializer.is_valid():
            SocialNetwork_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        social_network_data=JSONParser().parse(request)
        social_network=SocialNetwork.objects.get(idSocialNetwork=social_network_data['idSocialNetwork'])
        SocialNetwork_serializer=SocialNetworkSerializer(social_network,data=social_network_data)
        if SocialNetwork_serializer.is_valid():
            SocialNetwork_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        social_network=SocialNetwork.objects.get(idSocialNetwork=idSocialNetwork)
        social_network.delete()
        return JsonResponse("Deleted Successfully",safe=False)