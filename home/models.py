from django.db import models

class WebsiteSettings(models.Model):
    """
    Stores global settings like website name and logo.
    """
    website_name = models.CharField(max_length=100, default="Gym Records")
    logo = models.ImageField(upload_to="logos/", blank=True, null=True)

    def __str__(self):
        return self.website_name


class AboutUs(models.Model):
    """
    Stores the "About Us" page content.
    """
    title = models.CharField(max_length=200)
    content = models.TextField()
    banner_image = models.ImageField(upload_to="banners/", blank=True, null=True)

    def __str__(self):
        return self.title


class Feedback(models.Model):
    """
    Stores user feedback.
    """
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.created_at}"


class Banner(models.Model):
    """
    Stores banner images and descriptions.
    """
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="banners/")
    is_active = models.BooleanField(default=True)  # To enable/disable banners dynamically

    def __str__(self):
        return self.title