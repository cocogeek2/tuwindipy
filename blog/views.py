import json
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from blog.serializers import ArticleSerializer
from blog.models import Article
from category.models import Category
from category.serializers import CategorySerializer
from django.shortcuts import render
import requests


# Create your views here.
def articleDetails(request):
    details = requests.get('http://127.0.0.1:8000/article', {'idArticle':request.GET.get('idArticle')})
    return render(request, 'article_details.html', {
        'details': details.json })

def blog(request):
    articles = requests.get('http://127.0.0.1:8000/article')
    return render(request, 'articles.html', {'articles':articles.json})

def opportinuties(request):
    opp = requests.get('http://127.0.0.1:8000/article', {'category':'opportinutes'})
    return render(request, 'opportinuties.html', {'opportinutes':opp})

def projets(request):
    projets = requests.get('http://127.0.0.1:8000/article', {'category':'projets'})

    return render(request, 'projects.html', {'projects':projets.json})

def reports(request):
    reports = requests.get('http://127.0.0.1:8000/article', {'category':'rapports'})
    return render(request, 'rapports.html', {'rapports':reports})

def projetDetails(request):
    details = requests.get('http://127.0.0.1:8000/article', {'idArticle':request.GET.get('idArticle')})
    return render(request, 'project_details.html', {
        'details': details.json })

def reportDetails(request):
    details = requests.get('http://127.0.0.1:8000/article', {'idArticle':request.GET.get('idArticle')})
    return render(request, 'report_details.html', {
        'details': details.json })

@csrf_exempt
def ArticleApi(request, idArticle=0, category=""):
    if request.method == 'GET' and request.GET.get('idArticle') :
        id = int(request.GET.get('idArticle'))
        article=Article.objects.filter(idArticle=id)
        Article_serializer=ArticleSerializer(article,many=True)
        return JsonResponse(Article_serializer.data,safe=False)
    elif request.method == 'GET' and request.GET.get('category') :
        category = Category.objects.filter(libelle=request.GET.get('category'))
        categ_serializer = CategorySerializer(category,many=True)
        category = JsonResponse(categ_serializer.data,safe=False)
        for id in category :
            categ = json.loads(id)
        id = categ[0]['idCategory']
        article=Article.objects.filter(idCategory=id)
        Article_serializer=ArticleSerializer(article,many=True)
        return JsonResponse(Article_serializer.data,safe=False)
    elif request.method == 'GET':
        article = Article.objects.all()
        Article_serializer=ArticleSerializer(article,many=True)
        return JsonResponse(Article_serializer.data,safe=False)
    elif request.method=='POST':
        article_data=JSONParser().parse(request)
        Article_serializer=ArticleSerializer(data=article_data)
        if Article_serializer.is_valid():
            Article_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        article_data=JSONParser().parse(request)
        article=Article.objects.get(idArticle=article_data['idArticle'])
        Article_serializer=ArticleSerializer(article,data=article_data)
        if Article_serializer.is_valid():
            Article_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        article=Article.objects.get(idArticle=idArticle)
        article.delete()
        return JsonResponse("Deleted Successfully",safe=False)