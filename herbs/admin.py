from django.contrib import admin
from .models import Herb


class HerbAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )


admin.site.register(Herb, HerbAdmin)
