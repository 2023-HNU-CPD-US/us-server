# Generated by Django 4.1 on 2023-06-05 15:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usapp', '0003_folder_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='folder',
            name='user',
        ),
    ]
