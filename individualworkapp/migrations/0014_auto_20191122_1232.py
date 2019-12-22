# Generated by Django 2.2.6 on 2019-11-22 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('individualworkapp', '0013_teacher_citizenship'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='image',
            field=models.CharField(default=1, max_length=2000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='article',
            name='description',
            field=models.CharField(max_length=600),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
