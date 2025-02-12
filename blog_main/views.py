from django.shortcuts import render, redirect
from blogs.models import Category, Blog
from .forms import RegisterForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def home(request):
    featured_posts = Blog.objects.filter(is_featured=True, status="Published").order_by(
        "-updated_at"
    )[:6]
    posts = Blog.objects.filter(is_featured=False, status="Published")

    # Pagination
    paginator = Paginator(featured_posts, 3)
    print(f"paginator.num_pages : {paginator.num_pages}")
    page = request.GET.get("page")
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = {
        "featured_posts": featured_posts,
        "posts": posts,
    }
    return render(request, "home.html", context)


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("register")
    else:
        form = RegisterForm()
    context = {
        "form": form,
    }
    return render(request, "register.html", context)


def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)

            return redirect("dashboard")
    form = AuthenticationForm()
    context = {
        "form": form,
    }
    return render(request, "login.html", context)


def logout(request):
    auth.logout(request)
    return redirect("home")
