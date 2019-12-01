# Generated by Django 2.2.6 on 2019-11-30 17:58

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('UsersApp', '0027_auto_20191130_1753'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookings',
            name='bookingid',
            field=models.UUIDField(default=uuid.UUID('55a0bc33-c563-42fa-955e-618cbe2bcfb1'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='bookings',
            name='customer',
            field=models.CharField(max_length=100),
        ),
    ]
