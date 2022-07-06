from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from .models import News, Category
from .forms import CreateNews
# Create your views here.


class HomeNews(ListView):
    model = News
    template_name = 'news/index.html'
    context_object_name = 'news'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context

    def get_queryset(self):
        return News.objects.filter(is_published=True)


class NewsByCategory(ListView):
    model = News
    template_name = 'news/home_news_list.html'
    context_object_name = 'news'
    extra_context = {'categories': Category.objects.all()}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(pk=self.kwargs['category_id'])
        return context

    def get_queryset(self):
        return News.objects.filter(category_id=self.kwargs['category_id'],
                                   is_published=True)


def add_news(request):
    if request.method == 'POST':
        form = CreateNews(request.POST)
        if form.is_valid():
            news = form.save()
            return redirect(news)
    else:
        form = CreateNews()
    return render(request, 'news/add_news.html', {'form': form})

