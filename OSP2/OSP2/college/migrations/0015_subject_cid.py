# Generated by Django 3.2.5 on 2022-05-03 04:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0014_subject_susem'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='cid',
            field=models.ForeignKey(default='0', on_delete=django.db.models.deletion.CASCADE, to='college.college'),
        ),
    ]
