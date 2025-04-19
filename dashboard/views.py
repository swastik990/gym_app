from django.shortcuts import render
from dashboard.models import Category
from members.models import Member

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