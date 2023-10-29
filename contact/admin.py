from django.contrib import admin
from .models import ContactSubmission


class ContactSubmissionAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'email',
        'subject',
        'message',
        'created_at',
    )


admin.site.register(ContactSubmission, ContactSubmissionAdmin)
