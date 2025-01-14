from django.shortcuts import render, redirect
from .forms import LoginUser, RegisterUser
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User, Group


def loginUserInWeb(request):
    if request.method == "POST":
        form = LoginUser(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('public:home')
            else:
                return render(request, 'account/signin.html', {'form': form, 'error': 'Invalid email or password'})
    else:
        form = LoginUser()
    return render(request, 'account/signin.html', {'form': form})

def registerAction(request):
    if request.method == "POST":
        form = RegisterUser(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            if User.objects.filter(email=form.cleaned_data["email"]).exists():
                return render(request, 'account/signup.html', {'form': form, 'error': 'Email already exists'})
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.is_staff = False
                user.is_superuser = False
                user.save()
                customer_group, created = Group.objects.get_or_create(name="Customers")
                customer_group.user_set.add(user)
                return redirect('account:login')
        else:
            return render(request, 'account/signup.html', {'form': form})
    else:
        form = RegisterUser()
    return render(request, 'account/signup.html', {'form': form})

