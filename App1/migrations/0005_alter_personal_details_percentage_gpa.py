# Generated by Django 3.2.6 on 2021-09-09 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0004_alter_personal_details_percentage_gpa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personal_details',
            name='percentage_gpa',
            field=models.DecimalField(decimal_places=2, max_digits=4, null=True, verbose_name='Percentage/GPA'),
        ),
    ]
