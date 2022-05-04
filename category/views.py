from category.models import Category
from category.serializers import CategorySerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
# Create your views here.

@csrf_exempt
def CategoryApi(request, idCategory=0):
    if request.method == 'GET':
        category = Category.objects.all()
        Category_serializer=CategorySerializer(category,many=True)
        return JsonResponse(Category_serializer.data,safe=False)
    elif request.method=='POST':
        category_data=JSONParser().parse(request)
        Category_serializer=CategorySerializer(data=category_data)
        if Category_serializer.is_valid():
            Category_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        category_data=JSONParser().parse(request)
        category=Category.objects.get(idCategory=category_data['idCategory'])
        Category_serializer=CategorySerializer(category,data=category_data)
        if Category_serializer.is_valid():
            Category_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        category=Category.objects.get(idCategory=idCategory)
        category.delete()
        return JsonResponse("Deleted Successfully",safe=False)