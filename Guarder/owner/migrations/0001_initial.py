# Generated by Django 5.0.6 on 2025-04-07 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('owner_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=128)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]
