# Generated by Django 3.2.5 on 2022-05-02 08:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0005_todo'),
    ]

    operations = [
        migrations.AddField(
            model_name='branch',
            name='cid',
            field=models.ForeignKey(default='0', on_delete=django.db.models.deletion.CASCADE, to='college.college'),
        ),
        migrations.AlterField(
            model_name='branch',
            name='coid',
            field=models.ForeignKey(default='0', on_delete=django.db.models.deletion.CASCADE, to='college.course'),
        ),
    ]