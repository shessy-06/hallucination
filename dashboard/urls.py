from django.urls import path
from .views import home
from .views import home, contact, portfolio

urlpatterns = [
    path('', home, name='home'),
    path('contact/', contact, name='contact'),
    path('portfolio/', portfolio, name='portfolio'),
    
]