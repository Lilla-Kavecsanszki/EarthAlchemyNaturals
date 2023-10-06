from django.contrib import admin
from .models import Membership, VIPBox


class MembershipAdmin(admin.ModelAdmin):
    list_display = ('status',)


class VIPBoxAdmin(admin.ModelAdmin):
    list_display = ('selected_packaging_color',)


admin.site.register(Membership, MembershipAdmin)
admin.site.register(VIPBox, VIPBoxAdmin)
