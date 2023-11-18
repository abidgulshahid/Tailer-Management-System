# Generated by Django 4.2.5 on 2023-11-18 08:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tailer', '0003_customer_request_access'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='requestaccess',
            name='user',
        ),
        migrations.AddField(
            model_name='requestaccess',
            name='requested_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='request_by_usr', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='requestaccess',
            name='requested_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='request_to_user', to=settings.AUTH_USER_MODEL),
        ),
    ]