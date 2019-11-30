# Generated by Django 2.2.6 on 2019-11-30 12:56

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('UsersApp', '0024_auto_20191130_0956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookings',
            name='bookingid',
            field=models.UUIDField(default=uuid.UUID('44e4b742-46ac-40c9-ace3-ccd736689b3f'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='trips',
            name='destination',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='trips',
            name='duration',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='trips',
            name='startlocation',
            field=models.CharField(max_length=100),
        ),
    ]
