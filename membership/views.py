from django.shortcuts import render, redirect
from profiles.models import VIPBox
from django.contrib.auth.decorators import login_required
from products.models import Product
from datetime import timedelta, date
from profiles.models import UserProfile
from django.contrib import messages


def is_membership_valid(user):
    try:
        # Fetch the user's profile (for the membership details)
        user_profile = UserProfile.objects.get(user=user)

        # Check if the user has a membership start date
        membership_start_date = user_profile.membership_start_date

        if membership_start_date:
            # Calculate the expiration date by adding membership duration to
            # the start date
            expiration_date = (membership_start_date.date() +
                               timedelta(days=365))

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
        user_profile, created = UserProfile.objects.get_or_create(user=user)
        vip_box_choice = VIPBox.objects.filter(
            user_profile=user_profile).first()
        vip_box_color = (vip_box_choice.selected_packaging_color
                         if vip_box_choice else 'brown')

        context['vip_box_color'] = vip_box_color

        return render(request, 'membership_member.html', context)
    else:
        # Membership is expired or user is not logged in
        return render(request, 'membership.html', context)


@login_required
def create_vip_box(request):
    context = {}
    user = request.user
    user_profile, created = UserProfile.objects.get_or_create(user=user)
    vip_box_choice = VIPBox.objects.filter(
        user_profile=user_profile).first()
    vip_box_color = (vip_box_choice.selected_packaging_color
                     if vip_box_choice else 'brown')

    if request.method == 'POST':
        selected_packaging_color = request.POST.get('packaging_choice')

        # Check if the user already has the VIP box
        existing_vip_box, created = VIPBox.objects.get_or_create(
            user_profile=user_profile)

        # Update the existing VIP option
        existing_vip_box.selected_packaging_color = selected_packaging_color
        existing_vip_box.save()

        messages.success(
            request, 'Your VIP box choice has been updated successfully.')
        return redirect('create_vip_box')

    context['user'] = user
    context['vip_box_color'] = vip_box_color
    return render(request, 'membership_member.html', context)


@login_required
def delete_vip_box(request):
    user = request.user
    # Check if the user has a VIP box
    vip_box = VIPBox.objects.filter(user_profile__user=user).first()
    if vip_box:
        # Delete the VIP box
        vip_box.delete()
        messages.success(
            request, 'Your VIP box has been cancelled successfully.')
    else:
        messages.info(request, 'You do not have a VIP box to cancel.')
    return redirect('create_vip_box')
