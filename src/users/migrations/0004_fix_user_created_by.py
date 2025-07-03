# users/migrations/XXXX_fix_user_created_by.py
from django.db import migrations

def set_user_creators(apps, schema_editor):
    User = apps.get_model('users', 'User')
    
    # Get system user (should have been created by previous migrations)
    system_user = User.objects.get(uuid='00000000-0000-0000-0000-000000000000')
    
    # Set created_by for all users except system user itself
    User.objects.exclude(uuid=system_user.uuid).update(created_by=system_user)
    
    # For system user, set created_by to itself (or leave null if your model allows)
    system_user.created_by = system_user
    system_user.save()

class Migration(migrations.Migration):
    dependencies = [
        ('users', '0003_create_system_user'),  # Replace with your last users migration
    ]

    operations = [
        migrations.RunPython(set_user_creators),
    ]