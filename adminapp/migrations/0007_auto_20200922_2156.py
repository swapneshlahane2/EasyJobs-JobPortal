# Generated by Django 3.0.6 on 2020-09-22 16:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0003_users_email'),
        ('adminapp', '0006_auto_20200921_0930'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itjobs',
            name='user',
        ),
        migrations.AddField(
            model_name='itjobs',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='userapp.Users'),
        ),
    ]
