from django.shortcuts import render
from products.models import Categories



def index(request):
    categories = Categories.objects.all()
    context = {
        'title': 'Home',
        'content': 'Home page',
        'categories': categories,
    }
    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title': 'Home - О нас',
        'content': 'О нас',
        'text_on_page': 'Текст о нас'
    }
    return render(request, 'main/about.html', context)
