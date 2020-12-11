from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from users.forms import SignUpForm, UserProfileForm
from users.models import UserProfile


def register_user(request):
    if request.method == 'GET':
        context = {
            'form': SignUpForm(),
        }

        return render(request, 'users/registration_form.html', context)
    else:
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()
            profile = UserProfile(
                user=user,
            )
            profile.save()

            login(request, user)
            return redirect('current user profile')

        context = {
            'form': form,
        }

        return render(request, 'users/registration_form.html', context)


def user_profile(request, pk=None):
    user = request.user if pk is None else User.objects.get(pk=pk)
    if request.method == 'GET':
        context = {
            'profile_user': user,
            'profile': user.userprofile,
            # 'pets': user.userprofile.pet_set.all(),
            'form': UserProfileForm(),
        }

        return render(request, 'users/user_profile.html', context)
    else:
        form = UserProfileForm(request.POST, request.FILES, instance=user.userprofile)
        if form.is_valid():
            form.save()
            return redirect('current user profile')

        return redirect('current user profile')


def login_user(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect('home')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="users/login.html", context={"login_form": form})


def logout_user(request):
    logout(request)
    messages.info(request, 'You have successfully logged out.')
    return redirect('home')
