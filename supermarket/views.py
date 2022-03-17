from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
# Create your views here.
from django.utils import timezone

from accounts.models import User
from order.forms import UserNewOrderForm
from order.models import Basket, OrderDetail
from supermarket.models import Product, ProductGallery, SuperMarket, Category


def product_list(request, slug=None, smid=None):
    if slug and slug != "supermarket_category":
        products = Product.objects.filter(categories__slug__iexact=slug)
    elif slug == "supermarket_category" and smid != -1 and smid:
        supermarket = get_object_or_404(SuperMarket, id=smid)
        products = Product.objects.filter(super_market=supermarket)
    else:
        products = Product.objects.filter(active=True)
    paginator = Paginator(products, 3)  # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'supermarket/product-list.html', {'page_obj': page_obj})


def product_detail(request, pk):
    product = get_object_or_404(Product, id=pk)
    gallery = ProductGallery.objects.filter(product=product)
    new_order_form = UserNewOrderForm(initial={'product_id': product.id})
    context = {
        'product': product,
        'gallery': gallery,
        'new_order_form': new_order_form,
    }
    return render(request, 'supermarket/new-product-detail.html', context)
    # return render(request, 'supermarket/product-detail.html', context)


def category_list(request):
    all_category = Category.objects.all()  # last 6 category
    data = []
    temp = []
    counter = 0
    for item in all_category:
        if counter == 2:
            temp.append(item)
            data.append(temp)
            temp = []
            counter = 0
        elif item == all_category.last() and counter != 2:
            temp.append(item)
            data.append(temp)
            continue
        else:
            temp.append(item)
            counter += 1
    context = {
        'all_category': data,
        'user': request.user,
    }
    return render(request, 'supermarket/category-list.html', context)


@login_required(login_url="/accounts/login")
def order_list(request):
    if not request.user.is_authenticated or request.user.USER_TYPE != User.SuperMarketAdmin:
        return redirect('/')
    supermarket = SuperMarket.objects.filter(admin=request.user).first()
    if supermarket is None:
        return HttpResponse("<h2> You don't have supermarket")
    now = timezone.now()
    basket_list = Basket.objects.filter(delivery_time=now, user_selected_delivery_time__lt=5)
    order_detail_list = []
    for basket in basket_list:
        for order in OrderDetail.objects.filter(order=basket):
            if order.product.super_market == supermarket:
                order_detail_list.append(order)
    context = {
        'order_list': order_detail_list,
        'toDay': timezone.now().date()
    }
    return render(request, 'supermarket/order_list.html', context)
