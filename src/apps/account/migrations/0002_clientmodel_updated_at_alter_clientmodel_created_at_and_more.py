# Generated by Django 4.2.6 on 2025-01-06 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientmodel',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Update time'),
        ),
        migrations.AlterField(
            model_name='clientmodel',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Creation time'),
        ),
        migrations.DeleteModel(
            name='AccessControl',
        ),
    ]
