# Generated by Django 4.0 on 2022-03-28 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spaceapp', '0003_user_systems'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='systems',
        ),
        migrations.AddField(
            model_name='user',
            name='notes',
            field=models.ManyToManyField(to='spaceapp.Planet'),
        ),
    ]