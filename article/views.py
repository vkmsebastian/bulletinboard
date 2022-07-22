from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Article
from django.utils import timezone

def index(request):
    articles = Article.objects.order_by('-pub_date')
    return render(request, 'article/index.html', {'articles': articles})

def details(request, id):
    article = Article.objects.get(id=id)
    return render(request, 'article/details.html', {'article': article})

def create(request):
    if request.method == 'GET':
        return render(request, 'article/create.html')
        
    elif request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        pub_date = timezone.now()

        Article(title=title, content=content, pub_date=pub_date).save()
        return HttpResponseRedirect('/article')
    

def delete(request, id):
    a = Article.objects.get(id=id)
    a.delete()
    return HttpResponseRedirect('/article')

def edit(request, id):
    if request.method == 'GET':
        article = Article.objects.get(id=id)
        return render(request, 'article/edit.html', {'article': article})
    
    elif request.method == 'POST':
       a = Article.objects.get(id=id)
       a.title = request.POST['title']
       a.content = request.POST['content']
       a.save()
       return HttpResponseRedirect('/article')

