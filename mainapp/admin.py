from django.contrib import admin
from .models import News


class NewsAdmin(admin.ModelAdmin):
    list_display = (
        'emails',
    )


admin.site.register(News, NewsAdmin)
