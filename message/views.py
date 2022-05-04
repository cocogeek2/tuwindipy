from message.models import Message
from message.serializers import MessageSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
# Create your views here.

@csrf_exempt
def MessageApi(request, idMessage=0):
    if request.method == 'GET':
        message = Message.objects.all()
        Message_serializer=MessageSerializer(message,many=True)
        return JsonResponse(Message_serializer.data,safe=False)
    elif request.method=='POST':
        message_data=JSONParser().parse(request)
        Message_serializer=MessageSerializer(data=message_data)
        if Message_serializer.is_valid():
            Message_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        message_data=JSONParser().parse(request)
        message=Message.objects.get(idMessage=message_data['idMessage'])
        Message_serializer=MessageSerializer(message,data=message_data)
        if Message_serializer.is_valid():
            Message_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        message=Message.objects.get(idMessage=idMessage)
        message.delete()
        return JsonResponse("Deleted Successfully",safe=False)