from django.shortcuts import render
from webapp.articles_db import ArticlesDB
from django.http import HttpResponseRedirect


def index_view(request):
    articles = ArticlesDB.articles
    # print(request.GET)
    # print(request.GET.get('test'))
    # print(request.GET.get('name'))
    # print(request.GET.get('name2', 'test 123'))
    # print(request.GET.getlist('test'))
    return render(request, 'index.html', {'articles': articles})


def article_create_view(request):
    if request.method == "GET":
        return render(request, 'article_create.html')
    elif request.method == "POST":
        print(request.POST)
        article_new = {
            'title': request.POST.get('title'),
            'content': request.POST.get('content'),
            'author': request.POST.get('author'),
        }
        ArticlesDB.articles.append(article_new)
        return HttpResponseRedirect('/')
