from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from membership.views import is_membership_valid

from products.models import Product

# Create your views here.


def view_bag(request):
    """ A view that renders the bag contents page """
    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    product = Product.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})
    
    # Get the quantity from request.POST or default to 1 if it's not provided
    quantity_str = request.POST.get('quantity', '1')

    # Ensure quantity_str is a valid integer, defaulting to 1 if not
    try:
        quantity = int(quantity_str)
    except ValueError:
        quantity = 1

    # Check if the user is authenticated
    if request.user.is_authenticated:
        # Allow authenticated users to add any product to the bag
        if item_id in bag:
            bag[item_id]['quantity'] += quantity
        else:
            # Determine the price based on membership status
            has_valid_membership = is_membership_valid(request.user)
            if has_valid_membership:
                print("has valid membership")
                print("has valid membership")
                price = product.member_price
            else:
                price = product.price

            bag[item_id] = {
                'quantity': quantity,
                'price': str(price),
            }
            messages.success(request, f'Added {product.name} to your bag')
    else:
        # Prevent anonymous users from adding the membership product to the bag
        if product.sku == 'member100':
            messages.error(
                request, 'You must be logged in to purchase a membership.')
        else:
            if item_id in bag:
                bag[item_id] += quantity
            else:
                # For anonymous users, use the regular product price and quantity
                price = str(product.price)
                bag[item_id] = quantity
                messages.success(request, f'Added {product.name} to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """ Adjust the quantity of the specified product to the specified amount """

    product = Product.objects.get(pk=item_id)  # getting the product
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        if item_id in bag:
            bag[item_id] = quantity
        else:
            bag[item_id]['quantity'] = quantity
        messages.success(
            request, f'Updated {product.name} quantity to {quantity}')
    else:
        bag.pop(item_id, None)
        messages.success(request, f'Removed {product.name} from your bag')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """ Remove the item from the shopping bag """

    product = get_object_or_404(Product, pk=item_id)

    try:
        bag = request.session.get('bag', {})

        if item_id in bag:
            product_name = product.name  # getting the product name
            bag.pop(item_id, None)
            messages.success(request, f'Removed {product.name} from your bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
