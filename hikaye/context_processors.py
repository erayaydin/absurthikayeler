from .models import Category, Book

def categories(request):
    all_categories = Category.objects.all()

    return {
        'categories': all_categories,
    }

def popular(request):
    popularBooks = Book.objects.filter(type=True).order_by("-views")[:5]

    return {
        'popularBooks': popularBooks,
    }