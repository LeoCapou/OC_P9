# Generated by Django 3.0.14 on 2021-10-01 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_auto_20210930_2300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='time_created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]