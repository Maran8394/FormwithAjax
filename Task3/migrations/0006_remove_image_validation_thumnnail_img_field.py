# Generated by Django 3.2.6 on 2021-09-15 10:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Task3', '0005_image_validation_thumnnail_img_field'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image_validation',
            name='thumnnail_img_field',
        ),
    ]
