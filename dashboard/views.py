from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Category

def dashboard_view(request):
    # Fetch all categories with their member counts
    categories = Category.objects.all()
    context = {
        "categories": categories,
    }
    return render(request, "dashboard.html", context)

