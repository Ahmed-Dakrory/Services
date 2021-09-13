# Generated by Django 2.1.8 on 2021-09-12 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0021_auto_20210909_0118'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='country',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='region',
        ),
        migrations.AlterField(
            model_name='role',
            name='permissiongeneral',
            field=models.ManyToManyField(to='mainApp.permissiongeneral'),
        ),
        migrations.AlterField(
            model_name='theadd',
            name='images',
            field=models.ManyToManyField(to='mainApp.attachmenttranscript'),
        ),
    ]
