# Generated by Django 3.2.4 on 2021-06-21 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20210621_1628'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Desc',
        ),
        migrations.AddField(
            model_name='comp_detail',
            name='exp',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='expense',
            name='desc',
            field=models.CharField(blank=True, default='', max_length=500, null=True),
        ),
    ]
