# Generated by Django 2.2.6 on 2019-10-31 11:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('individualworkapp', '0005_auto_20191031_1247'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='specialization',
            name='specialization_code',
        ),
    ]
