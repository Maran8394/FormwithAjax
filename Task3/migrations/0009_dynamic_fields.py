# Generated by Django 3.2.6 on 2021-09-16 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Task3', '0008_auto_20210915_1732'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dynamic_fields',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interest', models.TextField(max_length=500, null=True)),
            ],
        ),
    ]
