from django.shortcuts import render
from .models import VIPBox
from django.contrib.auth.decorators import login_required
from products.models import Product
from datetime import datetime, timedelta
from django.shortcuts import render
from .models import Membership


def is_membership_valid(user):
    try:
        # Fetch the user's membership
        membership = Membership.objects.get(user=user)

        # Calculate the expiration date by adding 365 days to the created date
        expiration_date = membership.created_on + timedelta(days=365)

        # Fetch the current date
        today_date = datetime.now().date()

        # Check if the membership is still valid
        return today_date < expiration_date
    except Membership.DoesNotExist:
        # User doesn't have a membership, so it's not valid
        return False


def membership_view(request):
    # Fetch the membership product with SKU 'member100'
    member_product = Product.objects.filter(sku='member100').first()
    user = request.user if request.user.is_authenticated else None
    is_member = user and user.userprofile.membership_status == 'Member'

    if request.user.is_authenticated:
        is_valid_membership = is_membership_valid(user)
    else:
        is_valid_membership = False

    context = {
        'member_product': member_product,
        'is_member': is_member,
        'is_valid_membership': is_valid_membership,
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
