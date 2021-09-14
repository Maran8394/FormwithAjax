# Generated by Django 3.2.6 on 2021-09-13 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0007_auto_20210909_1855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personal_details',
            name='profile_pic',
            field=models.ImageField(null=True, upload_to='profile_pic', verbose_name='Profile picture'),
        ),
        migrations.AlterField(
            model_name='personal_details',
            name='upload_resume',
            field=models.FileField(null=True, upload_to='uploaded_resume', verbose_name='Upload resume'),
        ),
    ]
