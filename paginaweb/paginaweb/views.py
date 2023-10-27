from django.shortcuts import render, redirect
def home(req):
    ctx = {'nombre':'alo'}
    return render(req, 'test.html', ctx) 

def ayuda(req):
    ctx = {'nose':'que'}
    return render(req, 'ayuda.html', ctx)