from django.shortcuts import render
from .models import VIPBox
from django.contrib.auth.decorators import login_required
from products.models import Product
from datetime import datetime, timedelta, date
from django.shortcuts import render
from .models import Membership
from profiles.models import UserProfile


def is_membership_valid(user):
    try:
        # Fetch the user's profile (for the membership details)
        user_profile = UserProfile.objects.get(user=user)

        # Check if the user has a membership start date
        membership_start_date = user_profile.membership_start_date

        if membership_start_date:
            # Calculate the expiration date by adding membership duration to the start date
            expiration_date = membership_start_date.date() + timedelta(days=365)

            # Fetch the current date as a date object
            today_date = date.today()

            # Check if the membership is still valid
            return today_date < expiration_date

    except UserProfile.DoesNotExist:
        # User doesn't have a profile, so it's not valid
        return False

    # User doesn't have a valid membership start date, so it's not valid
    return False


def membership_view(request):
    # Fetch the membership product with SKU 'member100'
    member_product = Product.objects.filter(sku='member100').first()
    user = request.user if request.user.is_authenticated else None
    membership_start_date = None  # None for anonymous users

    if user:
        user_profile = UserProfile.objects.get(user=user)
        membership_start_date = user_profile.membership_start_date
        is_valid_membership = is_membership_valid(user)
    else:
        is_valid_membership = False

    context = {
        'member_product': member_product,
        'is_valid_membership': is_valid_membership,
        'membership_start_date': membership_start_date,
    }

    if is_valid_membership:
        # Valid membership
        return render(request, 'membership_member.html', context)
    else:
        # Membership is expired or user is not logged in
        return render(request, 'membership.html', context)



@login_required
def create_vip_box(request):
    context = {}

    if request.method == 'POST':
        selected_packaging_color = request.POST.get('selected_packaging_color')
        user = request.user

        # Check if the user already has the VIP box
        existing_vip_box = VIPBox.objects.filter(user=user).first()

        if existing_vip_box:
            # Update the existing VIP option
            existing_vip_box.selected_packaging_color = selected_packaging_color
            existing_vip_box.save()
        else:
            # Create a new VIP box
            vip_option = VIPBox(
                user=user, selected_packaging_color=selected_packaging_color)
            vip_option.save()

        return redirect('create_vip_box')
    else:
        context['user'] = request.user

        return render(request, 'create_vip_box', context)
