from django.shortcuts import render, get_object_or_404, redirect
from webapp.models import Article
from webapp.forms import ArticleForm
from django.views.generic import View, TemplateView


class IndexView(View):
    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()
        return render(request, 'index.html', {'articles': articles})


class ArticleView(TemplateView):
    template_name = 'article_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['article'] = get_object_or_404(Article, pk=kwargs.get('pk'))
        return context


def article_create_view(request):
    if request.method == "GET":
        form = ArticleForm()
        return render(request, 'article_create.html', {'form': form})
    elif request.method == "POST":
        form = ArticleForm(data=request.POST)

        if form.is_valid():
            article = Article.objects.create(
                title=form.cleaned_data.get('title'),
                content=form.cleaned_data.get('content'),
                author=form.cleaned_data.get('author')
            )
            return redirect('article_view', pk=article.pk)
        else:
            return render(request, 'article_create.html', {'form': form})


def article_update_view(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == "GET":
        form = ArticleForm(initial={
            'title': article.title,
            'content': article.content,
            'author': article.author
        })
        return render(request, 'article_update.html', {'form': form})
    elif request.method == "POST":

        form = ArticleForm(data=request.POST)
        if form.is_valid():
            article.title = form.cleaned_data.get('title')
            article.content = form.cleaned_data.get('content')
            article.author = form.cleaned_data.get('author')
            article.save()
            return redirect('article_view', pk=article.pk)
        else:
            return render(request, 'article_update.html', {'form': form})


def article_delete_view(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == "GET":
        return render(request, 'article_delete.html', {'article': article})
    elif request.method == 'POST':
        article.delete()
        return redirect('index')
