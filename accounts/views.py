from django.shortcuts import render, redirect
from django.contrib.auth import login, get_user_model, authenticate, logout
from accounts.forms import LoginForm, RegisterForm

# Create your views here


def login_user(request):
    if request.user.is_authenticated:
        return redirect('/')
    form = LoginForm(request.POST or None)

    if form.is_valid():
        user_name = form.cleaned_data.get('name')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=user_name, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            # login_form.add_error('user_name', 'user not found')
            pass

    context = {
        'form': form,
        'user': request.user,
    }
    return render(request, 'account/login.html', context)


def register(request):
    if request.user.is_authenticated:
        return redirect('/')
    register_form = RegisterForm(request.POST or None)

    if register_form.is_valid():
        user_name = register_form.cleaned_data.get('user_name')
        email = register_form.cleaned_data.get('email')
        phone_num = register_form.cleaned_data.get('phone_num')
        password = register_form.cleaned_data.get('password')
        User = get_user_model()
        User.objects.create_user(username=user_name, email=email, password=password, phone_num=phone_num)
        return redirect('accounts:login')

    context = {
        'form': register_form
    }
    return render(request, 'account/register.html', context)


def log_out(request):
    logout(request)
    return redirect("accounts:login")
