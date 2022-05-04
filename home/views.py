from django.shortcuts import render
import requests

# Create your views here.
def home(request):
    articles = requests.get('http://127.0.0.1:8000/article')
    bureaux = requests.get('http://127.0.0.1:8000/bureau')
    categories = requests.get('http://127.0.0.1:8000/category')
    projets = requests.get('http://127.0.0.1:8000/article?category=projets')
    chiffres = requests.get('http://127.0.0.1:8000/chiffre')
    comments = requests.get('http://127.0.0.1:8000/comment')
    domaines = requests.get('http://127.0.0.1:8000/domaine')
    infos = requests.get('http://127.0.0.1:8000/info')
    messages = requests.get('http://127.0.0.1:8000/message')
    rs = requests.get('http://127.0.0.1:8000/social_network')
    temoignages = requests.get('http://127.0.0.1:8000/temoignage')
    return render(request, 'home.html', {
        'articles': articles.json, 
        'bureaux': bureaux.json,
        'categories': categories.json,
        'projects': projets.json,
        'chiffres':chiffres.json,
        'comments':comments.json,
        'domaines':domaines.json,
        'infos':infos.json,
        'messages' : messages.json,
        'rs':rs.json,
        'temoignages':temoignages.json
    })

def about(request):
    rs = requests.get('http://127.0.0.1:8000/social_network')
    chiffres = requests.get('http://127.0.0.1:8000/chiffre')
    domaines = requests.get('http://127.0.0.1:8000/domaine')
    infos = requests.get('http://127.0.0.1:8000/info')
    return render(request, 'about.html', {        
        'domaines':domaines.json,
        'infos':infos.json,
        'chiffres':chiffres.json,
        'rs':rs.json,
    })
    
def contact(request):
    return render(request, 'contact.html', {})

def opportinutes(request):
    return render(request, 'opportinutes.html', {})