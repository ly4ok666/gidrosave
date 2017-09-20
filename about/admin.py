from django.contrib import admin
from .models import*
class AboutAdmin(admin.ModelAdmin):
    fields = [
        'about_title',
        'about_text',
        'about_image',

    ]
    list_display = ('about_title', 'about_image', 'bit')
admin.site.register(About, AboutAdmin)