# Generated by Django 3.2.6 on 2021-09-13 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0022_auto_20210913_1759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personal_details',
            name='gender',
            field=models.CharField(choices=[(1, 'Male'), ('Female', 'Female'), ('Other', 'Other')], default='Unspecified', max_length=10, null=True, verbose_name='Gender'),
        ),
        migrations.AlterField(
            model_name='personal_details',
            name='relationship_status',
            field=models.CharField(choices=[(1, 'Married'), (2, 'Unmarried')], default='Unspecified', max_length=100, null=True, verbose_name='Relationship status'),
        ),
    ]
