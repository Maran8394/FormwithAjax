# Generated by Django 3.2.6 on 2021-09-14 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0036_alter_personal_details_terms_conditions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personal_details',
            name='terms_conditions',
            field=models.BooleanField(null=True, verbose_name='Terms & Conditions'),
        ),
    ]