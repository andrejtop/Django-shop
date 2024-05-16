from django.core.paginator import Paginator
from django.shortcuts import render, get_list_or_404

from products.models import Products


def catalog(request, category_slug=None, page=1):
    if category_slug == "vse-tovary":
        goods = Products.objects.all()
    else:
        goods = get_list_or_404(Products.objects.filter(category__slug=category_slug))

    paginator = Paginator(goods, 3)
    current_page = paginator.page(page)
    context = {
        'title': 'Каталог',
        'goods': current_page,
        'slug_url': category_slug,
    }

    return render(request, 'products/catalog.html', context)


def product(request, product_slug):
    product = Products.objects.get(slug=product_slug)
    context = {
        'product': product
    }
    return render(request, 'products/product.html', context)
