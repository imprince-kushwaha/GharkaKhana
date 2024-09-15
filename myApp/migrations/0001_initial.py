# Generated by Django 4.2.6 on 2024-04-09 08:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=100)),
                ('user_mob', models.IntegerField(max_length=10)),
                ('user_desc', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Food_Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.CharField(max_length=10)),
                ('food_id', models.CharField(max_length=10)),
                ('food_type', models.CharField(max_length=100)),
                ('food_price', models.IntegerField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Food_Donation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('mobile', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=500)),
                ('description', models.CharField(max_length=200)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]