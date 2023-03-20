from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import SignupForm

# add error messages for user

def home(request):
    if request.method == 'POST':
        if 'signup' in request.POST:
            form = SignupForm(request.POST)
            if form.is_valid():
                email = form.cleaned_data.get('email')
                password = form.cleaned_data.get('password')
                try:
                    user = User.objects.create_user(username=email,password=password)
                    user.save()
                    messages.success(request, f'Account created for {email}!', extra_tags='acccreated')
                    return redirect('home')
                except:
                    messages.error(request, 'username exists, please login')
        elif 'signin' in request.POST:
            email = request.POST['email']
            password = request.POST['password']
            print(email,password)
            user = authenticate(username=email,password=password)
            print(user)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome {email}!')
                return redirect('main/')
            else:
                messages.error(request, 'Invalid email or password.')
    else:
        form = SignupForm(request.POST)
    return render(request, 'users/home.html')
