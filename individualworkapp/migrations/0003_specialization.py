# Generated by Django 2.2.6 on 2019-10-19 20:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('individualworkapp', '0002_auto_20191020_0032'),
    ]

    operations = [
        migrations.CreateModel(
            name='Specialization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('specialty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='individualworkapp.Specialty')),
            ],
        ),
    ]
