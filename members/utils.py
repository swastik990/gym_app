from django.core.exceptions import PermissionDenied
from login.models import Staff

def check_staff_category_permission(user, category_id):
    """
    Check if the logged-in staff has permission to access the given category.
    """
    if not user.is_authenticated or not hasattr(user, 'staff'):
        raise PermissionDenied("You do not have permission to access this page.")

    staff = user.staff
    if staff.category_id != category_id:
        raise PermissionDenied("You do not have permission to access this category.")