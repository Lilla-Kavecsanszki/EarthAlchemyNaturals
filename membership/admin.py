from django.contrib import admin
from .models import Membership


class MembershipAdmin(admin.ModelAdmin):
    list_display = ('status',)


admin.site.register(Membership, MembershipAdmin)
