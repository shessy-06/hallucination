from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import ContactMessage
from django.core.mail import send_mail

def home(request):
    return render(request, 'home.html')

def contact(request):

    if request.method == 'POST':

        name = request.POST.get('name')

        email = request.POST.get('email')

        message = request.POST.get('message')


        send_mail(

            subject='New Contact Message',

            message=f'''

Name: {name}

Email: {email}

Message:

{message}

''',

            from_email=email,

            recipient_list=[
                'thehallucinationfilms@gmail.com'
            ],

            fail_silently=False,
        )

    return render(request, 'contact.html')

def portfolio(request):

    return render(request, 'portfolio.html')