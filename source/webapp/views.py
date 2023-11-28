from django.shortcuts import render, get_object_or_404, reverse, redirect
from webapp.models import Article
from django.http import HttpResponseRedirect, HttpResponseNotFound, Http404


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
        article = Article.objects.create(
            title=request.POST.get('title'),
            content=request.POST.get('content'),
            author=request.POST.get('author')
        )
        # url = reverse('article_view', kwargs={'pk': article.pk})
        # print(url)
        # return HttpResponseRedirect(url)
        return redirect('article_view', pk=article.pk)
