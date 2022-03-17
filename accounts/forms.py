from django.contrib.auth.forms import UserCreationForm
from accounts.models import User
from django import forms


class CustomUserCreate(UserCreationForm):
    class Meta:
        model = User
        fields = "__all__"


class LoginForm(forms.Form):
    name = forms.CharField(label="User Name", max_length=100, min_length=4, widget=forms.TextInput(
        attrs={"class": "form-control"}))
    password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={"class": "form-control"}))


class AddPermission(forms.Form):
    name = forms.CharField(label='name', max_length=255)
    codename = forms.CharField(label='code name', max_length=100)


class RegisterForm(forms.Form):
    user_name = forms.CharField(label="user name", max_length=100, min_length=4, widget=forms.TextInput(
        attrs={"placeholder": "user name"}))
    email = forms.CharField(label="email", max_length=100, min_length=4, widget=forms.EmailInput(
        attrs={"placeholder": "email"}))
    phone_num = forms.CharField(label="phone number", max_length=100, min_length=4, widget=forms.TextInput(
        attrs={"placeholder": "phone number"}))
    password = forms.CharField(label="password", widget=forms.PasswordInput(
        attrs={"placeholder": "password"}))
    confirm_password = forms.CharField(label="confirm password", widget=forms.PasswordInput(
        attrs={"placeholder": "confirm password"}))

    def clean_email(self):
        email = self.cleaned_data.get('email')
        is_exists_user_by_email = User.objects.filter(email=email).exists()
        if is_exists_user_by_email:
            raise forms.ValidationError('Email entered before registering')
        return email

    def clean_user_name(self):
        user_name = self.cleaned_data.get('user_name')
        is_exists_user_by_username = User.objects.filter(username=user_name).exists()

        if is_exists_user_by_username:
            raise forms.ValidationError('Pre-selected username')

        return user_name

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError('Password and password confirm are not the same')
        return password
