from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

class About(models.Model):
    class Meta():
        db_table = 'about'
        verbose_name = u'О компании'
        verbose_name_plural = u'О компании'


    about_title = models.CharField(max_length=60, verbose_name=u'Заголовок')
    about_text = RichTextUploadingField(verbose_name=u'Текст')
    about_image = models.ImageField(null=True, blank=True, upload_to="images/",
                                      verbose_name=u'Изображение', )

    def __str__(self):
        return self.about_text[:50] + "..."

    def bit(self):
        if self.about_image:
            return u'<img src="%s" width="70"/>' % self.about_image.url
        else:
            return u'(none)'



    bit.short_descriptio = u'Изображение'
    bit.allow_tags = True


class ShortAbout(models.Model):
   class Meta():
       db_table = 'shortabout'

   short_text = models.TextField(verbose_name=u'Краткое описание')
   short_article = models.ForeignKey(About)