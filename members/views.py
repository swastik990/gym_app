from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from dashboard.models import Category
from .models import Member
from django.utils import timezone

def members_view(request, category_id):
    # Fetch the category and its members
    category = get_object_or_404(Category, id=category_id)
    members = category.members.all()
    context = {
        "category": category,
        "members": members,
    }
    return render(request, "members.html", context)

def add_member_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        category_id = request.POST.get("category")
        subscription_start_date = request.POST.get("subscription_start_date")
        subscription_end_date = request.POST.get("subscription_end_date")
        contact_info = request.POST.get("contact_info")

        # Validate and save the member
        category = get_object_or_404(Category, id=category_id)
        Member.objects.create(
            name=name,
            category=category,
            subscription_start_date=subscription_start_date,
            subscription_end_date=subscription_end_date,
            contact_info=contact_info,
        )
        messages.success(request, "Member added successfully.")
        return redirect("members", category_id=category_id)

    # Fetch all categories for the dropdown
    categories = Category.objects.all()
    context = {
        "categories": categories,
    }
    return render(request, "add_member.html", context)

def edit_member_view(request, member_id):
    member = get_object_or_404(Member, id=member_id)
    if request.method == "POST":
        member.name = request.POST.get("name")
        member.category_id = request.POST.get("category")
        member.subscription_start_date = request.POST.get("subscription_start_date")
        member.subscription_end_date = request.POST.get("subscription_end_date")
        member.contact_info = request.POST.get("contact_info")
        member.save()
        messages.success(request, "Member updated successfully.")
        return redirect("members", category_id=member.category_id)

    # Fetch all categories for the dropdown
    categories = Category.objects.all()
    context = {
        "member": member,
        "categories": categories,
    }
    return render(request, "add_member.html", context)

def delete_member_view(request, member_id):
    member = get_object_or_404(Member, id=member_id)
    category_id = member.category_id
    member.delete()
    messages.success(request, "Member deleted successfully.")
    return redirect("members", category_id=category_id)