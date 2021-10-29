from django.contrib import admin
from app.models import Paste


class PasteAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'content', 'date')

admin.site.register(Paste)