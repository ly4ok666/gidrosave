from django.shortcuts import render
from content.models import *

def article (request, article_id):
    article = Article.objects.get(id=article_id)
    return render(request, 'content/article.html', locals())