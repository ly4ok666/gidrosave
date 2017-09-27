from django.conf.urls import url
# from home.views import home
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    #стартовая страница
    # url(r'^$', home, name='home'),
    # # страница контента
    # url(r'^content/$', content, name='content'),
    # #конкретная статья
    # url(r'^content/get/(?P<article_id>\d+)/$', article, name='статья'),
    # #Все статьи
    # url(r'^content/articles/$', articles, name='articles'),
    # #Статьи по страницам
    # url(r'^articles/page/(\d+)/$', articles),
    # #Страница с контактами
    # url(r'^contacts/$', contacts, name='contacts'),



     ]
# url(r'^articles/all/$', articles),
if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns() + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)