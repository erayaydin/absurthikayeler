from django.shortcuts import render, redirect
from .forms import UserCreateForm
from django.contrib.auth.decorators import login_required

def register(request):
    if request.user.is_authenticated: redirect("/")

    form = UserCreateForm()
    if request.method == "POST":
        form = UserCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    return render(request, "register.html", { 'form': form })

@login_required
def profile(request):
    pass