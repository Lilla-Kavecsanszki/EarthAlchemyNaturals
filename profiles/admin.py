from django.contrib import admin
from .models import UserProfile, VIPBox


class UserProfileAdmin(admin.ModelAdmin):
    list_display = (
        'user', 'membership_status',
    )


class VIPBoxAdmin(admin.ModelAdmin):
    list_display = ('user_profile', 'selected_packaging_color',)


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(VIPBox, VIPBoxAdmin)
