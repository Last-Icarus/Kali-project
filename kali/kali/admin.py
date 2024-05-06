from django.contrib import admin
from . import views

class PageAdmin(admin.ModelAdmin):
    list_display = ('name', 'preview', 'likes', 'description')



admin.site.register(views.Art, PageAdmin)