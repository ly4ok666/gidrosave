from django.contrib import admin
from content.models import *

class ContentImagesInline (admin.TabularInline):
    model = ContentImages

class ArticlelInline(admin.StackedInline):
   model = Features
   extra = 0

class ArticleAdmin(admin.ModelAdmin):
    fields = [
        'article_title',
        'article_text',
        'article_date',
        # 'article_image',
        'video',
        'goals_1',
        'goals_2',

    ]
    list_display = ('article_title', 'article_date',)
    list_filter = [
        'article_date',
    ]
    inlines = [
            ArticlelInline,
            ContentImagesInline
        ]
admin.site.register(Article, ArticleAdmin)

class ContentImagesAdmin (admin.ModelAdmin):
    list_display = [field.name for field in ContentImages._meta.fields]

    class Meta:
        model = ContentImages

admin.site.register(ContentImages, ContentImagesAdmin)