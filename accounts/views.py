from django.shortcuts import render, redirect, HttpResponse
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def signin(request):
    if request.method == "GET":
        return render(request, 'accounts/signin.html')
    elif request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(
            request, 
            username=username,
            password=password
        )
        if user is not None:
            login(request, user)
            if user.is_superuser:
                return redirect('admin_index')
            elif user.is_staff:
                return redirect('pooler_index')
            else:
                messages.success(request, f'Welcome, {user}')
                return redirect('user_index')
        else:
            context = {}
            context['username'] = username
            messages.error(request, 'Invalid Username / Password')
            return render(request, 'accounts/signin.html')


def signup(request):
    if request.method == "GET":
        context = {}
        context['form1'] = UserForm()
        context['form2'] = UserExtraForm()
        context['form'] = 'user'
        return render(request, 'accounts/signup.html', context=context)
    elif request.method == "POST":
        user = UserForm(request.POST)
        userextra = UserExtraForm(request.POST)
        if user.is_valid() and userextra.is_valid():
            obj1 = user.save(commit=False)
            obj2 = userextra.save(commit=False)
            obj1.set_password(user.cleaned_data['password'])
            obj2.user = obj1
            obj1.save()
            obj2.save()
            messages.success(request, 'Account Successfully Created')
            return redirect('accounts_signin')
        else:
            context = {}
            context['form1'] = user
            context['form2'] = userextra
            messages.error(request, 'Please provide valid input')
            return render(request, 'accounts/signup.html', context=context)


def pooler_signup(request):
    if request.method == "GET":
        context = {}
        context['form1'] = UserForm()
        context['form2'] = PoolerForm()
        context['form'] = 'pooler'
        return render(request, 'accounts/pooler_signup.html', context=context)
    elif request.method == "POST":
        user = UserForm(request.POST)
        pooler = PoolerForm(request.POST, request.FILES)
        if user.is_valid() and pooler.is_valid():
            obj1 = user.save(commit=False)
            obj2 = pooler.save(commit=False)
            obj1.is_staff = True
            obj1.set_password(user.cleaned_data['password'])
            obj2.user = obj1
            obj1.save()
            obj2.save()
            messages.success(request, 'Account Successfully Created')
            return redirect('accounts_signin')
        else:
            context = {}
            context['form1'] = user
            context['form2'] = pooler
            messages.error(request, 'Please correct the error below.')
            return render(request, 'accounts/pooler_signup.html', context=context)

@login_required(login_url='accounts_signin')
def profile(request):
    if request.user.is_staff:
        instance1 = Pooler.objects.get(user=request.user)
        if request.method == "GET":
            context = {}
            context['form1'] = UserUpdateForm(instance=instance1.user)
            context['form2'] = PoolerForm(instance=instance1)
            return render(request, 'accounts/profile.html', context=context)
        elif request.method == "POST":
            user = UserUpdateForm(data=request.POST, instance=instance1.user)
            user_extra = PoolerForm(data=request.POST, instance=instance1, files=request.FILES)
            if user.is_valid() and user_extra.is_valid():
                user.save()
                user_extra.save()
                messages.success(request, 'Profile Information Updated Successfully')
                return redirect('accounts_profile')
            else:
                context = {}
                context['form1'] = user
                context['form2'] = user_extra
                messages.error(request, 'Please provide valid input')
                return render(request, 'accounts/profile.html', context=context)
    else:
        instance1 = UserExtra.objects.get(user=request.user)
        if request.method == "GET":
            context = {}
            context['form1'] = UserUpdateForm(instance=instance1.user)
            context['form2'] = UserExtraForm(instance=instance1)
            return render(request, 'accounts/profile.html', context=context)
        elif request.method == "POST":
            user = UserUpdateForm(data=request.POST, instance=instance1.user)
            user_extra = UserExtraForm(data=request.POST, instance=instance1)
            if user.is_valid() and user_extra.is_valid():
                user.save()
                user_extra.save()
                messages.success(request, 'Profile Information Updated Successfully')
                return redirect('accounts_profile')
            else:
                context = {}
                context['form1'] = user
                context['form2'] = user_extra
                messages.error(request, 'Please provide valid input')
                return render(request, 'accounts/profile.html', context=context)

@login_required(login_url='accounts_signin')
def change_password(request):
    if request.method == "GET":
        context = {}
        context['form'] = PasswordChangeForm(request.user)
        return render(request, 'accounts/change_password.html', context=context)
    elif request.method == "POST": 
        psw_form = PasswordChangeForm(request.user, request.POST)
        if psw_form.is_valid():
            user = psw_form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('accounts_change_password')
        else:
            messages.error(request, 'Please correct the error below.')
            context = {}
            context['form'] = psw_form
            return render(request, 'accounts/change_password.html', context=context)

def logout_action(request):
    logout(request)
    return redirect('accounts_signin')