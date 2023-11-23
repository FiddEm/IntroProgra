from django.shortcuts import render, redirect
from django.http import HttpResponse
import requests
from prueba.models import Posts
import uuid
import datetime
API_KEY = '5ae4eaf9df2e33659cfdb3eea941ee3a'
URL = 'https://api.meaningcloud.com/sentiment-2.1'

def home(req):
    return render(req, 'test.html', {})

def foro(req):
    posteos = Posts.getdata()
    return render(req, 'foro.html', {'posteos': posteos})


# mas adelante------
def post(req, post_id): 
    posteo = Posts.objects.get(post_id=post_id).text
    return HttpResponse(posteo)
#-------------------

def api(req):
    if req.method != 'POST':
        return redirect('/') # solo se usa post
    origin = req.headers['Referer']
    text = req.POST['comentario'] # comentario en dic
    params = {
        'key': API_KEY,
        'of': 'json',  
        'txt': text, 
        'lang': 'es'
    }
    response = requests.post(URL, params=params)
    if response.status_code == 200:
        data = response.json()
        sentimiento = data['score_tag']
        confianza = data['confidence']
    else: return HttpResponse('¡HUBO UN ERROR!')
    
    Posts.crearpost(text, sentimiento)
    
    return redirect(origin)


def ayuda(req):
    ctx = {'nose':'que'}
    return render(req, 'ayuda.html', ctx)