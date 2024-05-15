from django.shortcuts import render

from products.models import Products


def catalog(request):
    goods = Products.objects.all()
    context = {
        'title': 'Каталог',
        'goods': goods,
    }
    return render(request, 'products/catalog.html', context)


def product(request, product_id):
    product = Products.objects.get(id=product_id)
    context = {
        'product': product
    }
    return render(request, 'products/product.html', context)
