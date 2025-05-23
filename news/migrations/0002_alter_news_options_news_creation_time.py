# Generated by Django 5.2.1 on 2025-05-19 09:40

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ['-creation_time']},
        ),
        migrations.AddField(
            model_name='news',
            name='creation_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
