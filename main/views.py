from django.shortcuts import render
from products.models import Categories



def index(request):

    context = {
        'title': 'Home',
        'content': 'Home page',
    }
    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title': 'Home - О нас',
        'content': 'О нас',
        'text_on_page': 'Текст о нас'
    }
    return render(request, 'main/about.html', context)
