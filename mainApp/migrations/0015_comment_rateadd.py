# Generated by Django 2.1.8 on 2021-09-07 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0014_auto_20210907_1438'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='rateadd',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
