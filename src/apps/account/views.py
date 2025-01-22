from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpResponseRedirect
from .forms import LoginUser, RegisterUser
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User, Group
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def user_profile(request):
    return render(request, 'user_profile.html', {'user': request.user})


def loginUserInWeb(request):
    if request.method == "POST":
        form = LoginUser(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            print(f"Trying to authenticate user with email: {email}")
            user = authenticate(request, username=email, password=password)
            if user is not None:
                print("Authentication successful")
                login(request, user)
                return redirect('public:home')
            else:
                print("Invalid email or password")
                return render(request, 'account/signin.html', {'form': form, 'error': 'Invalid email or password'})
        else:
            print(f"Form is invalid: {form.errors}")
            return render(request, 'account/signin.html', {'form': form})
    else:
        form = LoginUser()
    return render(request, 'account/signin.html', {'form': form})


def registerAction(request):
    if request.method == "POST":
        form = RegisterUser(request.POST)
        if not form.is_valid():
            return render(request, 'account/signup.html', {'form': form, 'form_errors': form.errors})

        email = form.cleaned_data.get('email')
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')

        if User.objects.filter(email=email).exists():
            return render(request, 'account/signup.html', {'form': form, 'error': 'Email already exists'})

        try:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.is_staff = False
            user.is_superuser = False
            user.save()

            customer_group, created = Group.objects.get_or_create(name="Customers")
            customer_group.user_set.add(user)
        except Exception as e:
            return render(request, 'account/signup.html', {'form': form, 'error': f"An error occurred: {e}"})

        return redirect('account:login')
    else:
        form = RegisterUser()
    return render(request, 'account/signup.html', {'form': form})


def CheckLogin(request):
    if request.user.is_authenticated:
        return HttpResponse("وارد شده است")
    else:
        return HttpResponse("وارد نشده است")

def LogOutUser(request):
    logout(request)
    return HttpResponseRedirect("/Users/")
