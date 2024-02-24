# Generated by Django 4.1 on 2023-06-08 11:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usapp', '0006_rename_folder_text_parentid'),
    ]

    operations = [
        migrations.AddField(
            model_name='folder',
            name='parentId',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subfolders', to='usapp.folder'),
        ),
    ]