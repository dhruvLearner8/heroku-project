# Generated by Django 3.2.4 on 2021-06-22 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_desc_type1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='balance',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
        migrations.AlterField(
            model_name='expense',
            name='expense',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
        migrations.AlterField(
            model_name='expense',
            name='income',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
    ]