# Generated by Django 4.2.6 on 2024-04-13 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0003_alter_food_section_food_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=1000)),
                ('mob', models.IntegerField(max_length=10)),
                ('pin', models.IntegerField(max_length=8)),
                ('to_pay', models.IntegerField()),
            ],
        ),
    ]
