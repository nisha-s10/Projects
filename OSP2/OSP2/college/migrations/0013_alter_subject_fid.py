# Generated by Django 3.2.5 on 2022-05-02 15:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0012_alter_subject_fid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='fid',
            field=models.ForeignKey(blank=True, default='0', on_delete=django.db.models.deletion.CASCADE, to='college.faculty'),
        ),
    ]
