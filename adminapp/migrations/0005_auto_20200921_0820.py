# Generated by Django 3.0.6 on 2020-09-21 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0004_auto_20200921_0820'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itjobs',
            name='experience',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='itjobs',
            name='vaccancy',
            field=models.IntegerField(),
        ),
    ]
