# Generated by Django 4.1.7 on 2024-01-06 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='websiteinfo',
            name='hero_image',
            field=models.ImageField(upload_to='static/img'),
        ),
        migrations.AlterField(
            model_name='websiteinfo',
            name='logo',
            field=models.ImageField(upload_to='static/img/'),
        ),
    ]