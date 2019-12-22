# Generated by Django 2.2.6 on 2019-11-26 08:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('individualworkapp', '0022_student_specialty'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='specialization',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='individualworkapp.Specialization'),
        ),
    ]
