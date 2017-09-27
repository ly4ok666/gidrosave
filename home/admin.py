from django.contrib import admin
from home.models import*

# class HomeImglInline(admin.StackedInline):
#    model = HomeImg
#    extra = 2

class HomeAdmin(admin.ModelAdmin):
    fields = [
        'home_title',
        'home_text',
        'home_date',
        'home_image_1',
        'home_image_2',
        'home_image_3',
        'home_image_4',
        'home_image_5',
        'video',

    ]
    list_display = ('home_title', 'home_date',  'home_image_1', 'home_image_2', 'home_image_3', 'home_image_4', 'home_image_5',)
    list_filter = ['home_date']
    # inlines = [
    #         HomeImglInline
    #     ]
admin.site.register(Home, HomeAdmin)
