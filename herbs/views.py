from django.shortcuts import render, get_object_or_404
from .models import Herb

# Create your views here.


def star_ingredient(request, herb_id):
    """ To view the star ingredient details """

    herb = get_object_or_404(Herb, id=herb_id)

    context = {
        'herb': herb,
    }

    return render(request, 'herbs/herbs.html', context)
