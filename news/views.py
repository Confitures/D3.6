from django.shortcuts import render

# Create your views here.

# Импортируем класс, который говорит нам о том,
# что в этом представлении мы будем выводить список объектов из БД
from django.views.generic import ListView, DetailView
from .models import Post


class NewsList(ListView):
    # Указываем модель, объекты которой мы будем выводить
    model = Post
    # Выводиться будут только Новости, не статьи
    queryset = Post.objects.filter(item="news")
    # Поле, которое будет использоваться для сортировки объектов
    ordering = ['time_created', ]
    # Указываем имя шаблона, в котором будут все инструкции о том,
    # как именно пользователю должны быть показаны наши объекты
    template_name = 'flatpages/news.html'
    # Это имя списка, в котором будут лежать все объекты.
    # Его надо указать, чтобы обратиться к списку объектов в html-шаблоне.
    context_object_name = 'news'

class NewsDetail(DetailView):
    model = Post
    template_name = 'flatpages/news_detail.html'
    # context_object_name = 'news_detail'
    context_object_name = 'news'
