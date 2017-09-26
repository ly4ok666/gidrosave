from django.contrib import admin
from .models import*

class AboutlInline(admin.StackedInline):
   model = ShortAbout
   extra = 1

class AboutAdmin(admin.ModelAdmin):
    fields = [
        'about_title',
        'about_text',
        'about_image',

    ]
    list_display = ('about_title', 'about_image', 'bit')
    inlines = [
        AboutlInline
    ]
admin.site.register(About, AboutAdmin)