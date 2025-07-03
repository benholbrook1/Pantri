from users.models import User
from django.contrib import admin

# todo -- update / test save_model
class BaseModelAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):   
        if not change and not getattr(obj, "created_by_id", None):
            # Unwrap the user if it is a SimpleLazyObject
            user = request.user
            try:
                user = user._wrapped
            except AttributeError:
                pass
            
            if user.is_authenticated:
                obj.created_by_id = user.pk  # Assign by pk/id directly
            else:
                try:
                    default_user = User.objects.get(uuid="00000000-0000-0000-0000-000000000000")
                    obj.created_by_id = default_user.pk
                except User.DoesNotExist:
                    pass

        super().save_model(request, obj, form, change)



