from django.db import models
import uuid


class UUIDBaseModel(models.Model):

    def generate_uuid_str():
        return str(uuid.uuid4())

    uuid = models.CharField(
        primary_key=True,
        max_length=36,
        default=generate_uuid_str,
        editable=False,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey('users.User', on_delete=models.CASCADE, null=False, blank=True, editable=False)

    class Meta:
        abstract = True
