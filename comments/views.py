from comments.models import Comment
from comments.serializers import CommentSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
# Create your views here.

@csrf_exempt
def CommentApi(request, idComment=0):
    if request.method == 'GET':
        comment = Comment.objects.all()
        Comment_serializer=CommentSerializer(comment,many=True)
        return JsonResponse(Comment_serializer.data,safe=False)
    elif request.method=='POST':
        comment_data=JSONParser().parse(request)
        Comment_serializer=CommentSerializer(data=comment_data)
        if Comment_serializer.is_valid():
            Comment_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        comment_data=JSONParser().parse(request)
        comment=Comment.objects.get(idComment=comment_data['idComment'])
        Comment_serializer=CommentSerializer(comment,data=comment_data)
        if Comment_serializer.is_valid():
            Comment_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        comment=Comment.objects.get(idComment=idComment)
        comment.delete()
        return JsonResponse("Deleted Successfully",safe=False)