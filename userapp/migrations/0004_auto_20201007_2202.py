# Generated by Django 3.0.6 on 2020-10-07 16:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0012_auto_20201007_2152'),
        ('userapp', '0003_users_email'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Users',
            new_name='Usertable',
        ),
    ]
