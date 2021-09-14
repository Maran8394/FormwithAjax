# Generated by Django 3.2.6 on 2021-09-13 12:02

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0014_remove_personal_details_mobile'),
    ]

    operations = [
        migrations.AddField(
            model_name='personal_details',
            name='mobile',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, default=None, max_length=128, region=None),
        ),
    ]
