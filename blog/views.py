from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render
from blog.models import Article
from django.core.paginator import Paginator

def index(request):
    objs = Article.objects.all()
    paginator = Paginator(objs, 2)
    # paginatorを使って、queryParamaterのpageの値を取得する、という記述
    # https://exapmle.com?page=1 <- page=1 の部分に該当
    page_number = request.GET.get('page')
    context = {
        'page_obj': paginator.get_page(page_number),
        'page_number': page_number
    }
    return render(request, 'blog/blogs.html', context)

def article(request, pk):
    obj = Article.objects.get(pk=pk)
    context = {
        'article': obj,
    }
    return render(request, 'blog/article.html', context)
