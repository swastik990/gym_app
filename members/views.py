from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.utils import timezone
from dashboard.models import Category
from .models import Member, Subscription, Attendance
from django.contrib.auth.decorators import login_required
from .utils import check_staff_category_permission
from django.core.exceptions import PermissionDenied

@login_required
def members_view(request, category_id):
    # Check if the staff has permission to access this category
    check_staff_category_permission(request.user, category_id)

    category = get_object_or_404(Category, id=category_id)
    members = category.members.all()
    context = {"category": category, "members": members}
    return render(request, "members.html", context)


@login_required
def add_member_view(request):
    # Ensure the staff can only add members to their assigned category
    if not hasattr(request.user, 'staff') or not request.user.staff.category:
        raise PermissionDenied("You are not assigned to any category.")

    # Get the staff member's assigned category
    category = request.user.staff.category

    if request.method == "POST":
        name = request.POST.get("name")
        subscription_start_date = request.POST.get("subscription_start_date")
        subscription_end_date = request.POST.get("subscription_end_date")
        contact_info = request.POST.get("contact_info")

        # Convert date strings to datetime.date objects
        try:
            subscription_start_date = timezone.datetime.strptime(subscription_start_date, "%Y-%d-%m").date()
            subscription_end_date = timezone.datetime.strptime(subscription_end_date, "%Y-%d-%m").date()
        except ValueError:
            messages.error(request, "Invalid date format. Please use YYYY-MM-DD.")
            return redirect("add_member")

        # Create the member
        Member.objects.create(
            name=name,
            category=category,  # Use the staff member's assigned category
            subscription_start_date=subscription_start_date,
            subscription_end_date=subscription_end_date,
            contact_info=contact_info,
        )
        messages.success(request, "Member added successfully.")
        return redirect("members", category_id=category.id)

    # Pass the assigned category to the template
    context = {"category": category}
    return render(request, "add_member.html", context)

@login_required
def edit_member_view(request, member_id):
    member = get_object_or_404(Member, id=member_id)

    # Check if the staff has permission to edit this member
    check_staff_category_permission(request.user, member.category_id)

    if request.method == "POST":
        member.name = request.POST.get("name")
        member.subscription_start_date = timezone.datetime.strptime(
            request.POST.get("subscription_start_date"), "%Y-%m-%d"
        ).date()
        member.subscription_end_date = timezone.datetime.strptime(
            request.POST.get("subscription_end_date"), "%Y-%m-%d"
        ).date()
        member.contact_info = request.POST.get("contact_info")
        member.save()
        messages.success(request, "Member updated successfully.")
        return redirect("members", category_id=member.category_id)

    context = {"member": member}
    return render(request, "add_member.html", context)

@login_required
def delete_member_view(request, member_id):
    member = get_object_or_404(Member, id=member_id)

    # Check if the staff has permission to delete this member
    check_staff_category_permission(request.user, member.category_id)

    category_id = member.category_id
    member.delete()
    messages.success(request, "Member deleted successfully.")
    return redirect("members", category_id=category_id)

# Add a subscription record
def add_subscription_view(request, member_id):
    member = get_object_or_404(Member, id=member_id)
    if request.method == "POST":
        start_date = request.POST.get("start_date")
        end_date = request.POST.get("end_date")
        amount_paid = request.POST.get("amount_paid")
        payment_status = request.POST.get("payment_status")

        Subscription.objects.create(
            member=member,
            start_date=start_date,
            end_date=end_date,
            amount_paid=amount_paid,
            payment_status=payment_status,
        )
        messages.success(request, "Subscription added successfully.")
        return redirect("members", category_id=member.category_id)

    context = {"member": member}
    return render(request, "add_subscription.html", context)

# Mark attendance
def mark_attendance_view(request, member_id):
    member = get_object_or_404(Member, id=member_id)
    if request.method == "POST":
        check_in_time = request.POST.get("check_in_time")
        check_out_time = request.POST.get("check_out_time")

        Attendance.objects.create(
            member=member,
            check_in_time=check_in_time,
            check_out_time=check_out_time,
        )
        messages.success(request, "Attendance marked successfully.")
        return redirect("members", category_id=member.category_id)

    context = {"member": member}
    return render(request, "mark_attendance.html", context)