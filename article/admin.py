from django.contrib import admin
from .models import*

# class ArticlelInline(admin.StackedInline):
#    model = Features
#    extra = 2

class BlogAdmin(admin.ModelAdmin):
    fields = [
        'article_title',
        'article_text',
        'short_text',
        'article_date',
        'article_image',
        'video',
        # 'goals_1',
        # 'goals_2',

    ]
    list_display = ('article_title', 'article_date', 'article_image', 'bit',)
    list_filter = [
        'article_date',
    ]
    # inlines = [
    #         ArticlelInline
    #     ]
admin.site.register(Blog, BlogAdmin)