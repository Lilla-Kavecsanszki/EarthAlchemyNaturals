from django.shortcuts import render
from .models import VIPBox
from django.contrib.auth.decorators import login_required
from products.models import Product


def membership_view(request):
    # Fetch the membersip product with SKU 'member100'
    member_product = Product.objects.filter(sku='member100').first()
    user = request.user if request.user.is_authenticated else None
    is_member = user and user.userprofile.membership_status == 'Member'

    context = {
        'member_product': member_product,
        'is_member': is_member,
    }
    
    if is_member:
        template_name = 'membership_member.html'
    else:
        template_name = 'membership.html'

    return render(request, template_name, context)



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
