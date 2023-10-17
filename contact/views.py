from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm


def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            send_mail(
                form.cleaned_data['subject'],  # subject
                f"Message from {form.cleaned_data['name']} "
                f"<{form.cleaned_data['email']}>\n\n"
                f"{form.cleaned_data['message']}",  # message
                None,  # from email
                ['earthalchemynaturals@example.com'],
            )
            messages.success(
                request,
                'Thank you for submitting! We will be in touch soon!')
            return redirect('contact_us')

    else:
        form = ContactForm()

    return render(request, 'contact_us.html', {'form': form})
