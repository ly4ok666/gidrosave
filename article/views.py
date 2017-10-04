from django.shortcuts import render
from article.models import *

def blogpost (request, article_id):
    article = Blog.objects.get(id=article_id)
    return render(request, 'article/blogpost.html', locals())