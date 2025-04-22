from django.contrib import admin
from . import models

# Register your models here.

registered_models = [models.WebsiteSettings, models.AboutUs, models.Feedback, models.Banner]

admin.site.register(registered_models)
