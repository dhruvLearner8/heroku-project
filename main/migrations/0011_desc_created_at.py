# Generated by Django 3.2.4 on 2021-06-29 10:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20210624_0933'),
    ]

    operations = [
        migrations.AddField(
            model_name='desc',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]