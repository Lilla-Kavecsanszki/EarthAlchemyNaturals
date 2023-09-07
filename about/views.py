from django.shortcuts import render

# Create your views here.


def aboutus(request):
    """ A view to return the about us page """

    return render(request, 'about/aboutus.html')
