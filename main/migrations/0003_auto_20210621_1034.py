# Generated by Django 3.2.4 on 2021-06-21 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_expense'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='balance',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='expense',
            name='desc',
            field=models.CharField(blank=True, default='', max_length=500, null=True),
        ),
    ]