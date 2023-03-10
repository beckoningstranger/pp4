# Generated by Django 3.2.16 on 2023-01-28 19:48

import django.contrib.postgres.fields
from django.db import migrations, models
import timeline.models


class Migration(migrations.Migration):

    dependencies = [
        ('timeline', '0015_alter_socialuser_following'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialuser',
            name='following',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), blank=True, default=timeline.models.set_default_following, null=True, size=None),
        ),
    ]
