from django.contrib import admin
from . import views

class PageAdmin(admin.ModelAdmin):
    list_display = ('name', 'preview', 'likes', 'description')

class UserSettings(admin.ModelAdmin):
    list_display = ('user_id', 'no_ai_tag', 'bio', 'avatar', 'header')

admin.site.register(views.Art, PageAdmin)
admin.site.register(views.UserSettings, UserSettings)