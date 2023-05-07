from django.shortcuts import render

# Простая главная страница для примера
def home_page(request, uri=None):
    context = {
        'menuURL': '',
    }
    if uri:
        context['menuURL'] = uri
    return render(request, "menu.html", context)