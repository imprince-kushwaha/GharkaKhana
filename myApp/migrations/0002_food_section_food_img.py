# Generated by Django 4.2.6 on 2024-04-09 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='food_section',
            name='food_img',
            field=models.ImageField(default=False, upload_to=''),
        ),
    ]
