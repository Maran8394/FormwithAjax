# Generated by Django 3.2.6 on 2021-09-14 11:05

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0030_alter_personal_details_percentage_gpa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personal_details',
            name='mobile',
            field=phonenumber_field.modelfields.PhoneNumberField(default='+91', max_length=128, null=True, region=None, verbose_name='Mobile Number'),
        ),
    ]
