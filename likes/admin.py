from django.contrib import admin
from .models import HowMuchLike


class HowMuchLikeAdmin(admin.ModelAdmin):
    list_display = (
        'like',
        'feedback',
    )


admin.site.register(HowMuchLike, HowMuchLikeAdmin)
