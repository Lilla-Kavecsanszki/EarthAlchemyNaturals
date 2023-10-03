from django.shortcuts import render
from .models import VIPBox
from django.contrib.auth.decorators import login_required
from products.models import Product


def membership_view(request):
    # Fetch the membersip product with SKU 'member100'
    member_product = Product.objects.filter(sku='member100').first()

    context = {
        'member_product': member_product
    }

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

        return redirect('profile')
    else:
        context['user'] = request.user

        return render(request, 'profile', context)
