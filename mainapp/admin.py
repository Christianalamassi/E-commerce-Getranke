from django.contrib import admin
from .models import News

# Register your models here.

class NewsAdmin(admin.ModelAdmin):
    list_display = (
        'emails',
    )


admin.site.register(News, NewsAdmin)