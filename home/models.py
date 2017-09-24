from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from embed_video.fields import EmbedVideoField


class Home(models.Model):
    home_title = models.CharField(max_length=60, verbose_name='Заголовок')
    home_text = RichTextUploadingField(verbose_name='Текст статьи')
    # можно нафик убрать время или вообще всё
    home_date = models.DateTimeField(verbose_name="Дата и время")
    home_image = models.ImageField(null=True, blank=True, upload_to="images/",
                                      verbose_name=u'Изображение', )
    video = EmbedVideoField(null=True, blank=True, verbose_name=u'Видео', )


    def __str__(self):
        return self.home_text

    def bit(self):
        if self.home_image:
            return u'<img src="%s" width="70"/>' % self.home_image.url
        else:
            return u'(none)'

    bit.short_descriptio = u'Изображение'
    bit.allow_tags = True
    class Meta():
        db_table = "home"
        verbose_name = 'статьи'
        verbose_name_plural = 'статьи'
        ordering = ['-home_date']

# class Header(models.Model):
#    class Meta():
#        db_table = 'features'
#        verbose_name = 'статьи'
#
#    header_img
#    features_text = models.TextField()
#
#    features_article = models.ForeignKey(Home)



