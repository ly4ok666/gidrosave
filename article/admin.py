from django.contrib import admin
from .models import*

class BlogImagesInline (admin.TabularInline):
    model = BlogImages
# class ArticlelInline(admin.StackedInline):
#    model = Features
#    extra = 2

class BlogAdmin(admin.ModelAdmin):
    fields = [
        'article_title',
        'article_text',
        'short_text',
        'article_date',
        # 'article_image',
        'video',
        # 'goals_1',
        # 'goals_2',

    ]
    list_display = ('article_title', 'article_date',)
    list_filter = [
        'article_date',
    ]
    inlines = [
        BlogImagesInline
    ]
admin.site.register(Blog, BlogAdmin)

class BlogImagesAdmin (admin.ModelAdmin):
    list_display = [field.name for field in BlogImages._meta.fields]

    class Meta:
        model = BlogImages

admin.site.register(BlogImages, BlogImagesAdmin)