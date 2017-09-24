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


def home(request):
    """Домашняя страница нашего проекта"""
    contexts = Home.objects.all()
    # краткое о нас
    context = About.objects.all()
    return render(request, 'index.html', locals())

def about(request):
    """Страница о компании"""
    context = About.objects.all()
    return render(request, 'about.html', locals())

def content(request,article_id=1):
    # article = {'article': Article.objects.get(id=article_id)}
    #Вывод всех статей и пагинация (2 статьи на страницу)"""
    # краткое о нас
    abouts = About.objects.all()
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
    # краткое о нас
    abouts = About.objects.all()
    # articles = Article.objects.get(id=article_id)
    # features = Features.objects.filter(features_article_id=article_id)
    # return render(request, 'home/article.html', locals())
    return render_to_response('home/articles.html', {'article': Article.objects.get(id=article_id),
                                               'features': Features.objects.filter(features_article_id=article_id),
                                               'abouts': abouts})

    # new imports that go at the top of the file
from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.template import Context
from django.template.loader import get_template

    # our view
def contact(request):
    abouts = About.objects.all()
    form_class = ContactForm
         # new logic!
    if request.method == 'POST':
        form = form_class(data=request.POST)
        if form.is_valid():
            contact_name = request.POST.get('contact_name', '')
            contact_email = request.POST.get('contact_email', '')
            form_content = request.POST.get('content', '')
                # Email the profile with the
                # contact information
            template = get_template('contact_template.txt')
            context = {'contact_name': contact_name, 'contact_email': contact_email, 'form_content': form_content}
            content = template.render(context)
            email = EmailMessage("New contact form submission", content, "Your website" + '', ['ly4ok666@gmail.com'], headers={'Reply-To': contact_email})
            email.send()
        # return render('contact')
        # Переходим на другую страницу, если сообщение отправлено
#         return HttpResponseRedirect('/contacts/thanks/')
    return render(request, 'contacts/contacts.html', {
        'form': form_class,'abouts': abouts,})
#
# def thanks(reguest):
#     thanks = 'thanks'
#     return render(reguest, 'thanks.html', {'thanks': thanks})