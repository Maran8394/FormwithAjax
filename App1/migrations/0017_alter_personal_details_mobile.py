# Generated by Django 3.2.6 on 2021-09-13 12:03

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0016_alter_personal_details_mobile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personal_details',
            name='mobile',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, null=True, region=None),
        ),
    ]