# Generated by Django 3.2.16 on 2023-01-21 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timeline', '0008_alter_post_images'),
    ]

    operations = [
        migrations.AddField(
            model_name='socialuser',
            name='profile_image',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='post',
            name='excerpt',
            field=models.CharField(max_length=500),
        ),
    ]
