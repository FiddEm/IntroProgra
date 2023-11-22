from django.db import models
import uuid
import datetime

IMAGEN = {
    'P': '/static/img/feliz.svg',
    'P+': '/static/img/feliz.svg', #feliz
    'N': '/static/img/triste.svg', # triste
    'NEU': '/static/img/neutro.svg', # neutro
    'NONE': '/static/img/help.svg', #NADA
}
    
class Posts(models.Model):
    post_id = models.UUIDField(null=False)
    sentimiento = models.CharField(max_length=10, default='NONE')
    likes = models.IntegerField(default=0)
    date = models.DateField(null=False)
    comentario = models.CharField(max_length=99999, default='[]')
    text = models.CharField(max_length=10000, null=False)
    def getdata():
        posteos = Posts.objects.order_by('date')[::-1][:3]
        datos = []
        for posteo in posteos:
            dato = {
                'post_id':posteo.post_id,
                'sentimiento': posteo.sentimiento,
                'likes': posteo.likes,
                'date': posteo.date,
                'comentario': posteo.comentario,
                'text': posteo.text,
                'img': IMAGEN[posteo.sentimiento],
            }
            datos.append(dato)
        return datos 
    def crearpost(text, sentimiento):
        post_id = uuid.uuid4()
        date = datetime.datetime.now()
        Posts.objects.create(text=text, sentimiento=sentimiento, post_id=post_id, date=date)
        


