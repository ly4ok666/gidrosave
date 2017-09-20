from django.shortcuts import render
from django.http.response import HttpResponse
from .forms import ContactForm
from django.http.response import HttpResponseRedirect
from django.core.mail import send_mail, BadHeaderError
# #from django.template.loader import get_template
# #from django.template import Context
from django.shortcuts import render_to_response
from home.models import Home
from about.models import About
from content.models import Article, Features
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# from about_card.models import Card
# from start.models import StartContent
# from end.models import EndContent

# Create your views here.

def home(request):
    """Домашняя страница нашего проекта"""
    contexts = Home.objects.all()
    return render(request, 'index.html', locals())

def about(request):
    """Страница о компании"""
    context = About.objects.all()
    return render(request, 'about.html', locals())

def content(request,article_id=1):
    # article = {'article': Article.objects.get(id=article_id)}
    #Вывод всех статей и пагинация (2 статьи на страницу)"""
    all_Articles = Article.objects.all()
    paginator = Paginator(all_Articles, 4)
    page = request.GET.get('page')

    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)
    context = {'articles': articles}
    return render(request, 'content.html', locals())

def article(request, article_id=1):
    """Вывод одной конкретной статьи """
    # articles = Article.objects.get(id=article_id)
    # features = Features.objects.filter(features_article_id=article_id)
    # return render(request, 'home/article.html', locals())
    return render_to_response('home/articles.html', {'article': Article.objects.get(id=article_id),
                                               'features': Features.objects.filter(features_article_id=article_id),
                                               })

# Функция формы обратной связи
def contacts(reguest):
    if reguest.method == 'POST':
        form = ContactForm(reguest.POST)
        # Если форма заполнена корректно, сохраняем все введённые пользователем значения
        if form.is_valid():
            subject = form.cleaned_data['subject']
            sender = form.cleaned_data['sender']
            message = form.cleaned_data['message']
            copy = form.cleaned_data['copy']

            recepients = ['sender']
            # Если пользователь захотел получить копию себе, добавляем его в список получателей
            if copy:
                recepients.append(sender)
            try:
                send_mail(subject, message, '', recepients)
            except BadHeaderError: #Защита от уязвимости
                return HttpResponse('Invalid header found')
            # Переходим на другую страницу, если сообщение отправлено
            return HttpResponseRedirect('/contacts/thanks/')

    else:
        form = ContactForm()
    # Выводим форму в шаблон
    return render(reguest, 'contacts/contacts.html', {'form': form})

def thanks(reguest):
    thanks = 'thanks'
    return render(reguest, 'thanks.html', {'thanks': thanks})