# Generated by Django 2.2.6 on 2019-11-29 08:05

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('UsersApp', '0018_auto_20191129_0750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookings',
            name='bookingid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
