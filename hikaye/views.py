from django.shortcuts import render, redirect
from .models import Book, Category
from django.contrib.auth.decorators import login_required

from .forms import BookCreateForm, CommentForm

def bookIndex(request):
    if "q" in request.GET:
        books = Book.objects.filter(title__icontains=request.GET["q"]).filter(type=True)
    else:
        books = Book.objects.filter(type=True)
    return render(request, "index.html", { "books": books })

def bookShow(request, book_id):
    commentform = CommentForm()
    book = Book.objects.get(pk=book_id)
    if request.method == "POST":
        commentform = CommentForm(request.POST)

        if commentform.is_valid():
            comment = commentform.save(commit=False)
            comment.type = False
            comment.parent = book
            comment.author = request.user
            comment.title = book.title
            comment.save()
    return render(request, "show.html", { "book": book, "commentform": commentform })

def categoryShow(request, category_id):
    category = Category.objects.get(pk=category_id)
    return render(request, "category.html", { "category": category, "books": category.books.filter(parent=None) })

@login_required
def newBook(request, parent_id=None):
    form = BookCreateForm()
    if request.method == "POST":
        form = BookCreateForm(request.POST)

        if form.is_valid():
            newbook = form.save(commit=False)
            newbook.author = request.user
            if parent_id != None:
                newbook.parent = Book.objects.get(pk=parent_id)
                newbook.type = True
            newbook.save()
            form.save_m2m()
            return redirect('/')

    return render(request, "create.html", {
        "form": form
    })