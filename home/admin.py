from django.contrib import admin
from home.models import Home


class HomeAdmin(admin.ModelAdmin):
    fields = [
        'home_title',
        'home_text',
        'home_date',
        'home_image',
        'video',

    ]
    list_display = ('home_title', 'home_date', 'home_image', 'bit',)
    list_filter = ['home_date']
admin.site.register(Home, HomeAdmin)
