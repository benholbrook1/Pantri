from django.db import models
import uuid

# Create your models here.
class UUIDBaseModel(models.Model):

    def generate_uuid_str():
        return str(uuid.uuid4())

    uuid = models.CharField(primary_key=True, max_length=36, default=generate_uuid_str, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True