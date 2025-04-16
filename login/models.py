from django.db import models
from django.contrib.auth.models import User

class Staff(models.Model):
    """
    Represents additional staff accounts created by the gym owner.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="created_staff")

    def __str__(self):
        return self.user.username