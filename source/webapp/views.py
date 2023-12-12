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


class ArticleCreateView(View):
    def get(self, request, *args, **kwargs):
        form = ArticleForm()
        return render(request, 'article_create.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = ArticleForm(data=request.POST)

        if form.is_valid():
            tags = form.cleaned_data.pop('tags')
            article = Article.objects.create(
                title=form.cleaned_data.get('title'),
                content=form.cleaned_data.get('content'),
                author=form.cleaned_data.get('author'),
            )
            article.tags.set(tags)
            return redirect('article_view', pk=article.pk)
        else:
            return render(request, 'article_create.html', {'form': form})


class ArticleUpdateView(TemplateView):
    template_name = 'article_update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        article = get_object_or_404(Article, pk=kwargs.get('pk'))
        form = ArticleForm(initial={
            'title': article.title,
            'content': article.content,
            'author': article.author,
            'tags': article.tags.all()
        })
        context['form'] = form
        return context

    def post(self, request, *args, **kwargs):
        article = get_object_or_404(Article, pk=kwargs.get('pk'))
        form = ArticleForm(data=request.POST)
        if form.is_valid():
            tags = form.cleaned_data.pop('tags')
            article.title = form.cleaned_data.get('title')
            article.content = form.cleaned_data.get('content')
            article.author = form.cleaned_data.get('author')
            article.tags.set(tags)
            article.save()
            return redirect('article_view', pk=article.pk)
        else:
            return render(request, 'article_update.html', {'form': form})


class ArticleDeleteView(View):
    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, pk=kwargs.get('pk'))
        return render(request, 'article_delete.html', {'article': article})

    def post(self, request, *args, **kwargs):
        article = get_object_or_404(Article, pk=kwargs.get('pk'))
        article.delete()
        return redirect('index')
