# Generated by Django 3.0.6 on 2020-09-23 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0003_users_email'),
        ('adminapp', '0007_auto_20200922_2156'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itjobs',
            name='user',
        ),
        migrations.AddField(
            model_name='itjobs',
            name='user',
            field=models.ManyToManyField(to='userapp.Users'),
        ),
    ]
