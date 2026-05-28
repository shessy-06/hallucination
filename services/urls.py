from django.urls import path

from .views import (
    wedding,
    advertisement,
    shortfilms,
    photoshoot,
    modelphotography,   
    productphotography
)

urlpatterns = [

    path(
        'wedding/',
        wedding,
        name='wedding'
    ),

    path(
        'advertisement/',
        advertisement,
        name='advertisement'
    ),

    path(
        'shortfilms/',
        shortfilms,
        name='shortfilms'
    ),

    path(
        'photoshoot/',
        photoshoot,
        name='photoshoot'
    ),

    path(
        'model-photography/',
        modelphotography,
        name='model_photography'
    ),

    path(
        'product-photography/',
        productphotography,
        name='product_photography'
    ),

]