# Generated by Django 3.2.5 on 2022-05-02 09:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0006_auto_20220502_1341'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('suname', models.CharField(max_length=50)),
                ('brid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='college.branch')),
                ('coid', models.ForeignKey(default='0', on_delete=django.db.models.deletion.CASCADE, to='college.course')),
            ],
        ),
    ]