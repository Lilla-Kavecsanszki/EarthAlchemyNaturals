from django.shortcuts import render, redirect, reverse

# Create your views here.


def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    print = None
    if 'product_print' in request.POST:
        print = request.POST['product_print']
    bag = request.session.get('bag', {})

    if print:
        if item_id in list(bag.keys()):
            if print in bag[item_id]['items_by_print'].keys():
                bag[item_id]['items_by_print'][print] += quantity
            else:
                bag[item_id]['items_by_print'][print] = quantity
        else:
            bag[item_id] = {'items_by_print': {print: quantity}}
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
        else:
            bag[item_id] = quantity

    request.session['bag'] = bag
    return redirect(redirect_url)
