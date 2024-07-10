from django.contrib import admin
from .models import HowMuchLike

# Register your models here.

class HowMuchLikeAdmin(admin.ModelAdmin):
    list_display = (
        'like',
        'feedback',
    )


admin.site.register(HowMuchLike, HowMuchLikeAdmin)