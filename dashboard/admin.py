from django.contrib import admin
from . import models

# Register your models here.

registered_models = [models.Category]

admin.site.register(registered_models)
