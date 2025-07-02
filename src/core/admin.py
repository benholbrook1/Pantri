from users.models import User
from . import admin

# todo
# class BaseModelAdmin(admin.ModelAdmin):
#     def save_model(self, request, obj, form, change):
#         if not change and hasattr(obj, "created_by") and not obj.created_by:
#             # Ensure the request.user is the User instance, not Django's default User
#             if isinstance(request.user, User):
#                 obj.created_by = request.user
#             else:
#                 # fallback to your default system user
#                 try:
#                     default_user = User.objects.get(uuid="00000000-0000-0000-0000-000000000000")
#                     obj.created_by = default_user
#                 except User.DoesNotExist:
#                     pass
#         super().save_model(request, obj, form, change)