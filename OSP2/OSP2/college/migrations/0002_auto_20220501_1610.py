# Generated by Django 3.2.5 on 2022-05-01 10:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brname', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coname', models.CharField(max_length=20)),
                ('cid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='college.college')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rolno', models.CharField(default='0', max_length=50)),
                ('sem', models.CharField(default='0', max_length=50)),
                ('sname', models.CharField(default='', max_length=50)),
                ('semail', models.CharField(default='', max_length=50)),
                ('smob', models.CharField(default='', max_length=12)),
                ('swa', models.CharField(default='', max_length=12)),
                ('sadd', models.CharField(default='', max_length=100)),
                ('scity', models.CharField(default='', max_length=50)),
                ('sdesc', models.CharField(default='', max_length=500)),
                ('penass', models.CharField(default='0', max_length=10)),
                ('simg', models.ImageField(default='college/Screenshot.png', upload_to='student/')),
                ('sstatus', models.CharField(blank=True, max_length=10)),
                ('spass', models.CharField(default='12345', max_length=50)),
                ('brid', models.ForeignKey(default='0', on_delete=django.db.models.deletion.CASCADE, to='college.branch')),
                ('coid', models.ForeignKey(default='0', on_delete=django.db.models.deletion.CASCADE, to='college.course')),
            ],
        ),
        migrations.AddField(
            model_name='branch',
            name='coid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='college.course'),
        ),
    ]