from django.shortcuts import render
from supermarket.models import Category, SuperMarket


# Create your views here.

def home(request):
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
    return render(request, 'main/index.html', context)


def home(request):
    supermarkets = SuperMarket.objects.all()
    data = []
    temp = []
    counter = 0
    for item in supermarkets:
        if counter == 2:
            temp.append(item)
            data.append(temp)
            temp = []
            counter = 0
        elif item == supermarkets.last() and counter != 2:
            temp.append(item)
            data.append(temp)
            continue
        else:
            temp.append(item)
            counter += 1
    context = {
        'supermarkets': data,
    }
    return render(request, 'main/index.html', context)
