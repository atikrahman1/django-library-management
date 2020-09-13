# Generated by Django 3.0.8 on 2020-07-19 22:31

import dashboard.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0007_auto_20200720_0129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='cover',
            field=models.ImageField(blank=True, default='default.png', null=True, upload_to=dashboard.models.update_filename),
        ),
        migrations.AlterField(
            model_name='books',
            name='description',
            field=models.TextField(max_length=200),
        ),
    ]
