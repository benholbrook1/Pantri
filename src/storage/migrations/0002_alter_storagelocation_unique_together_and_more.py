# Generated by Django 5.2.3 on 2025-06-28 01:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='storagelocation',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='storagelocation',
            name='created_by',
        ),
    ]
