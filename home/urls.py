from django.conf.urls import url
from home.views import home
from home.views import about
from home.views import content
from home.views import article
from home.views import contact
from home.views import blog
from home.views import blogpost
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    # стартовая страница
    url(r'^$', home, name='home'),
    # страница о компании
    url(r'^about-us/$', about, name='about'),
    #конкретная статья
    url(r'^content/get/(?P<article_id>\d+)/$', article, name='статья'),
    #Все статьи
     url(r'^content/$', content, name='articles'),
    # Все статьи блога
    url(r'^articles/$', blog, name='blog'),
    #Статьи по страницам блога
    url(r'^articles/page/(\d+)/$', blog),
    #конкретная статья блога
    url(r'^articles/get/(?P<article_id>\d+)/$', blogpost, name='статья'),
    #Страница с контактами
    url(r'^contact/$', contact, name='contact'),
     ]
# url(r'^articles/all/$', articles),
if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns() + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)