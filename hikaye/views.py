from django.shortcuts import render
from .models import Book, Category
from django.contrib.auth.decorators import login_required

def bookIndex(request):
    books = Book.objects.filter(parent=None)
    return render(request, "index.html", { "books": books })

def bookShow(request, book_id):
    book = Book.objects.get(pk=book_id)
    return render(request, "show.html", { "book": book })

def categoryShow(request, category_id):
    category = Category.objects.get(pk=category_id)
    return render(request, "category.html", { "category": category, "books": category.books.filter(parent=None) })

@login_required
def newBook(request):
    return render(request, "create.html")

@login_required
def newBookFromParent(request, parent_id):
    pass