# Generated by Django 3.2.6 on 2021-09-13 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0011_alter_personal_details_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personal_details',
            name='TelePhone',
            field=models.IntegerField(default=None, null=True, verbose_name='TelePhone'),
        ),
    ]