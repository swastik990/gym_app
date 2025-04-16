from django.contrib import admin
from . import models

# Register your models here.
registered_models = [models.Member, models.MemberInfo, models.Subscription, models.Attendance]

admin.site.register(registered_models)
