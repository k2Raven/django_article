from django.shortcuts import render, get_object_or_404, reverse, redirect
from webapp.models import Article
from webapp.validate_char_field import article_validate


def index_view(request):
    articles = Article.objects.all()
    return render(request, 'index.html', {'articles': articles})


def article_view(request, *args, pk, **kwargs):
    # print(kwargs)
    # article_id = kwargs.get('pk')
    # print(article_id)
    # print(pk)
    # try:
    #     article = Article.objects.get(id=pk)
    # except Article.DoesNotExist:
    #     # return HttpResponseNotFound('Not Found')
    #     raise Http404()
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'article_view.html', {'article': article})


def article_create_view(request):
    if request.method == "GET":
        return render(request, 'article_create.html')
    elif request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        author = request.POST.get('author')
        article = Article(title=title, content=content, author=author)
        errors = article_validate(title, content, author)

        if errors:
            return render(request, 'article_create.html', {'errors': errors, 'article': article})
        else:
            article.save()
            return redirect('article_view', pk=article.pk)


def article_update_view(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == "GET":
        return render(request, 'article_update.html', {'article': article})
    elif request.method == "POST":

        article.title = request.POST.get('title')
        article.content = request.POST.get('content')
        article.author = request.POST.get('author')
        errors = article_validate(article.title, article.content,  article.author)

        if errors:
            return render(request, 'article_update.html', {'errors': errors, 'article': article})
        else:
            article.save()
            return redirect('article_view', pk=article.pk)


def article_delete_view(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == "GET":
        return render(request, 'article_delete.html', {'article': article})
    elif request.method == 'POST':
        article.delete()
        return redirect('index')
