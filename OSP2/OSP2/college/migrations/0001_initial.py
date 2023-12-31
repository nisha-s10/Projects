# Generated by Django 3.2.5 on 2022-05-01 07:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='College',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=50)),
                ('cemail', models.CharField(max_length=50)),
                ('cmob', models.CharField(max_length=12)),
                ('cadd', models.CharField(max_length=100)),
                ('ccity', models.CharField(max_length=50)),
                ('cweb', models.CharField(max_length=50)),
                ('cdesc', models.CharField(max_length=500)),
                ('cimg', models.ImageField(default='college/Screenshot.png', upload_to='college/')),
                ('cstatus', models.CharField(blank=True, max_length=10)),
                ('cpass', models.CharField(default='12345', max_length=50)),
                ('uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='college.university')),
            ],
        ),
    ]
