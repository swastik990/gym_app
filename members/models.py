from django.db import models
from django.utils import timezone
from dashboard.models import Category  # Import Category from the dashboard app

class Member(models.Model):
    """
    Represents individual gym members.
    """
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('disabled', 'Disabled (Quit)'),
        ('delayed', 'Delayed (Fee Not Paid)'),
    ]

    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="members")
    subscription_start_date = models.DateField()
    subscription_end_date = models.DateField()
    contact_info = models.CharField(max_length=15, blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active')

    def is_subscription_expired(self):
        """
        Check if the subscription has expired.
        """
        return timezone.now().date() > self.subscription_end_date

    def save(self, *args, **kwargs):
        """
        Automatically update the status based on subscription dates.
        """
        if self.is_subscription_expired():
            self.status = 'delayed'  # Mark as delayed if subscription has expired
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class MemberInfo(models.Model):
    """
    Stores detailed personal information and history for each member.
    """
    member = models.OneToOneField(Member, on_delete=models.CASCADE, related_name="info")
    date_of_birth = models.DateField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    emergency_contact = models.CharField(max_length=15, blank=True, null=True)
    medical_history = models.TextField(blank=True, null=True, help_text="Any medical conditions or allergies.")
    notes = models.TextField(blank=True, null=True, help_text="Additional notes about the member.")

    def __str__(self):
        return f"Info for {self.member.name}"


class Subscription(models.Model):
    """
    Tracks the subscription history of a member (e.g., renewals, changes).
    """
    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name="subscription_history")
    start_date = models.DateField()
    end_date = models.DateField()
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    payment_status = models.CharField(max_length=20, choices=[('paid', 'Paid'), ('pending', 'Pending')], default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.member.name} - {self.start_date} to {self.end_date}"


class Attendance(models.Model):
    """
    Tracks daily attendance of members.
    """
    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name="attendance")
    date = models.DateField(default=timezone.now)
    check_in_time = models.TimeField(null=True, blank=True)
    check_out_time = models.TimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.member.name} - {self.date}"