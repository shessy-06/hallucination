from django.shortcuts import render


def wedding(request):

    return render(request, 'services/wedding.html')


def advertisement(request):

    return render(request, 'services/advertisement.html')


def shortfilms(request):

    return render(request, 'services/shortfilms.html')

def photoshoot(request):

    return render(request, 'services/photoshoot.html')

def modelphotography(request):

    return render(request, 'services/model_photography.html')

def productphotography(request):

    return render(request, 'services/product_photography.html')