from django import forms


class UserNewOrderForm(forms.Form):
    product_id = forms.IntegerField(
        widget=forms.HiddenInput(),
    )

    count = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control text-center w-100'}),
        initial=1

    )


TO_DAY_GEEKS_CHOICES = (
    ("17", "17-18"),
    ("18", "18-19"),
    ("19", "19-20"),
    ("20", "20-21"),
    ("21", "21-22"),
)

TOMORROW_GEEKS_CHOICES = (
    ("11", "11-12"),
    ("12", "12-13"),
    ("13", "13-14"),
    ("14", "14-15"),
    ("15", "15-16"),
    ("16", "16-17"),
    ("17", "17-18"),
    ("18", "18-19"),
    ("19", "19-20"),
    ("20", "20-21"),
    ("21", "21-22"),
)


class ToDayBasketForm(forms.Form):
    post_code = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control form-control-lg"}),
    )
    address = forms.CharField(
        widget=forms.Textarea(attrs={"class": "form-control form-control-lg"}),
    )
    deliver_time = forms.ChoiceField(choices=TO_DAY_GEEKS_CHOICES,
                                     widget=forms.Select(attrs={"class": "form-select"}))


class TomorrowBasketForm(forms.Form):
    post_code = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control form-control-lg"}),
    )
    address = forms.CharField(
        widget=forms.Textarea(attrs={"class": "form-control form-control-lg"}),
    )
    deliver_time = forms.ChoiceField(choices=TOMORROW_GEEKS_CHOICES,
                                     widget=forms.Select(attrs={"class": "form-select"}))


class PaymentForm(forms.Form):
    card_number = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    card_password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
    )
    basket_id = forms.IntegerField()
