# Generated by Django 3.2.6 on 2021-09-15 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Task3', '0002_rename_img_image_validation_img_field'),
    ]

    operations = [
        migrations.AddField(
            model_name='image_validation',
            name='img_h',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='image_validation',
            name='img_w',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
