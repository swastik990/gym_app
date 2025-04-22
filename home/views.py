from django.shortcuts import render, redirect
from django.contrib import messages
from .models import WebsiteSettings, AboutUs, Banner, Feedback

def home_view(request):
    # Fetch dynamic content
    website_settings = WebsiteSettings.objects.first() or WebsiteSettings.objects.create()
    about_us = AboutUs.objects.first()
    active_banners = Banner.objects.filter(is_active=True)

    context = {
        "website_settings": website_settings,
        "about_us": about_us,
        "active_banners": active_banners,
    }
    return render(request, "index.html", context)

def submit_feedback_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        Feedback.objects.create(name=name, email=email, message=message)
        messages.success(request, "Thank you for your feedback!")
        return redirect("home")
    return redirect("home")
