from django.db import models
from django.contrib.auth.models import User
from dashboard.models import Category

class Staff(models.Model):
    """
    Represents additional staff accounts created by the gym owner.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name="staff_members")
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="created_staff")

    def __str__(self):
        return self.user.username