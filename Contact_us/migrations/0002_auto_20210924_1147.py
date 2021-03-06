# Generated by Django 3.2.6 on 2021-09-24 06:17

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Contact_us', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact_us',
            old_name='email',
            new_name='email_id',
        ),
        migrations.RenameField(
            model_name='contact_us',
            old_name='resume',
            new_name='resume_file',
        ),
        migrations.RenameField(
            model_name='contact_us',
            old_name='name',
            new_name='user_name',
        ),
        migrations.RemoveField(
            model_name='contact_us',
            name='mobile',
        ),
        migrations.AddField(
            model_name='contact_us',
            name='mobile_num',
            field=models.IntegerField(null=True, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(10)]),
        ),
    ]
