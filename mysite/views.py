import imp
from django.shortcuts import render
from blog.models import Article

def index(request):
  objs = Article.objects.all()[:3]
  context = {
      'title': 'Really site!!',
      'articles': objs,
  }
  return render(request, 'mysite/index.html', context)
