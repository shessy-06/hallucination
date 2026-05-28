from django.shortcuts import render, redirect
from .models import CustomUser
from django.contrib.auth import authenticate, login, logout



# REGISTER

def register(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # CREATE USER

        CustomUser.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        # AFTER REGISTER REDIRECT TO LOGIN PAGE

        return redirect('login')

    return render(request, 'accounts/register.html')




# LOGIN

def login_view(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            # AFTER LOGIN

            return redirect('/projects/create/')

    return render(request, 'accounts/login.html')




# LOGOUT

def logout_view(request):

    logout(request)

    return redirect('/')