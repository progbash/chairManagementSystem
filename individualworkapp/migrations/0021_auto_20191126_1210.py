# Generated by Django 2.2.6 on 2019-11-26 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('individualworkapp', '0020_cgroup_specialization'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='birth_year',
            field=models.DateField(),
        ),
    ]
