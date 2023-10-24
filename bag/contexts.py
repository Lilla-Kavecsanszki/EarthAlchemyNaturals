from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product
from membership.views import is_membership_valid


def bag_contents(request):
    bag_items = []
    total = 0
    discount_amount = 0
    product_count = 0
    bag = request.session.get('bag', {})

    # Check if the user has a valid membership and set the discount percentage
    # accordingly
    if request.user.is_authenticated:
        has_valid_membership = is_membership_valid(request.user)
    else:
        has_valid_membership = False  # Not authenticated, so not a valid

    if has_valid_membership:
        discount_percentage = 30  # 30% discount for members
    else:
        discount_percentage = 0  # No discount for non-members

    for item_id, item_data in bag.items():
        if isinstance(item_data, int):
            product = get_object_or_404(Product, pk=item_id)
            # Apply the discount to the product price if applicable
            discounted_price = product.price - \
                (product.price * discount_percentage / 100)
            total += item_data * discounted_price
            product_count += item_data
            bag_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'product': product,
                'discounted_price': round(discounted_price, 2)
            })
            # Calculate the discount amount for this item and add it to
            # the total discount amount
            item_discount_amount = product.price - discounted_price
            discount_amount += item_discount_amount * item_data

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

    context = {
        'bag_items': bag_items,
        'total': round(total, 2),
        'product_count': product_count,
        'delivery': round(delivery, 2),
        'free_delivery_delta': round(free_delivery_delta, 2),
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': round(grand_total, 2),
        'discount_percentage': discount_percentage,
        'discount_amount': round(discount_amount, 2),  # total discount applied
    }

    return context
