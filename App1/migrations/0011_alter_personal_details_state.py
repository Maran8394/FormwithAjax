# Generated by Django 3.2.6 on 2021-09-13 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0010_alter_personal_details_mobile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personal_details',
            name='state',
            field=models.CharField(blank=True, default=None, max_length=100, verbose_name='State'),
        ),
    ]
