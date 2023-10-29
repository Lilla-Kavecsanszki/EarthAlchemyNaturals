from django.shortcuts import render


def aboutus(request):
    """ A view to return the about us page """

    return render(request, 'about/aboutus.html')
