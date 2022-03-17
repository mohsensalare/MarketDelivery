from datetime import datetime, timedelta
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.utils import timezone
# Create your views here.
from order.forms import UserNewOrderForm, ToDayBasketForm, TomorrowBasketForm, PaymentForm
from order.models import Basket, OrderDetail
from supermarket.models import Product


@login_required(login_url="/accounts/login")
def add_user_order(request):
    new_order_form = UserNewOrderForm(request.POST or None)
    if new_order_form.is_valid():
        user = request.user
        product_id = new_order_form.cleaned_data.get("product_id")
        count = new_order_form.cleaned_data.get("count")
        basket = Basket.objects.filter(owner=user, is_paid=False).first()
        if basket is None:
            basket = Basket.objects.create(owner=user, is_paid=False)
        if count < 0:
            count = 1
        product = get_object_or_404(Product, id=product_id)
        order_detail = basket.orderdetail_set.filter(product=product, order=basket).first()
        if order_detail is None:
            basket.orderdetail_set.create(product=product, order=basket, count=count)
        else:
            order_detail.count += count
        return redirect(product.get_absolute_url)
    return redirect("/")


@login_required(login_url="/accounts/login")
def basket(request):
    now = timezone.now()
    if now.hour < 12:
        form = ToDayBasketForm(request.POST or None)
        timee = datetime.now()
    else:
        form = TomorrowBasketForm(request.POST or None)
        timee = datetime.now() + timedelta(days=1)
    user_basket = request.user.baskets.filter(is_paid=False, status="1").first()
    if user_basket is None:
        user_basket = Basket.objects.create(owner=request.user)
    if form.is_valid():
        user_basket.user_selected_delivery_time = form.cleaned_data.get('deliver_time')
        user_basket.delivery_time = timee.date()
        user_basket.address = form.cleaned_data.get('post_code') + " " + form.cleaned_data.get('address')
        user_basket.save()
        return redirect(reverse('order:payment', kwargs={"basket_id": user_basket.id}))
    context = {
        "order": user_basket.orderdetail_set.all(),
        'basket': user_basket,
        "form": form
    }
    return render(request, "order/basket.html", context)


@login_required(login_url="/accounts/login")
def remove_order_detail(request, *args, **kwargs):
    detail_id = kwargs.get('detail_id')
    if detail_id is not None:
        order_detail = OrderDetail.objects.get_queryset().get(id=detail_id, order__owner_id=request.user.id)
        if order_detail is not None:
            order_detail.delete()
            return redirect(reverse('order:basket'))
    raise Http404()


@login_required(login_url="/accounts/login")
def fake_payment(request, *args, **kwargs):
    basket_id = kwargs.get('basket_id')
    user_basket = Basket.objects.get(id=basket_id)
    form = PaymentForm(initial={'basket_id': user_basket.id})
    context = {
        "form": form,
        "basket": user_basket
    }
    return render(request, "order/payment.html", context)


@login_required(login_url="/accounts/login")
def fake_payment_done(request, *args, **kwargs):
    basket_id = kwargs.get('basket_id')
    user_basket = Basket.objects.get(id=basket_id)
    user_basket.status = '2'
    user_basket.is_paid = True
    user_basket.payment_date = timezone.now()
    user_basket.save()
    return redirect('/')
