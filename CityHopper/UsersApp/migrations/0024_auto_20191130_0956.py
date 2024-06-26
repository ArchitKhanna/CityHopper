# Generated by Django 2.2.6 on 2019-11-30 09:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('UsersApp', '0023_auto_20191129_0827'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookings',
            name='customer',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='bookings',
            name='bookingid',
            field=models.UUIDField(default=uuid.UUID('c74d135a-1e69-4062-8468-8c778758239a'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
