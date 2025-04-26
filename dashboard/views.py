from django.shortcuts import render, redirect
from .models import Category
from members.models import Member
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test

def dashboard_view(request):
    # Fetch all categories with their member counts
    categories = Category.objects.all()
    total_members = Member.objects.count()
    active_members = Member.objects.filter(status="active").count()
    disabled_members = Member.objects.filter(status="disabled").count()

    context = {
        "categories": categories,
        "total_members": total_members,
        "active_members": active_members,
        "disabled_members": disabled_members,
    }
    return render(request, "dashboard.html", context)

from django.contrib.auth.decorators import user_passes_test

@user_passes_test(lambda u: u.is_superuser)
def create_category_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        Category.objects.create(name=name)
        messages.success(request, "Category created successfully.")
        return redirect("dashboard")
    return render(request, "create_category.html")