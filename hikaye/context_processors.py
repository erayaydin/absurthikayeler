from .models import Category

def categories(request):
    all_categories = Category.objects.all()

    return {
        'categories': all_categories,
    }