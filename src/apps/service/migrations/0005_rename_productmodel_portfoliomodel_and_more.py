# Generated by Django 4.2.6 on 2025-01-07 13:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0004_remove_servicemodel_description_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ProductModel',
            new_name='PortfolioModel',
        ),
        migrations.AddField(
            model_name='categorymodel',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Creation time'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='categorymodel',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Update time'),
        ),
        migrations.AddField(
            model_name='servicemodel',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Creation time'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='servicemodel',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Update time'),
        ),
    ]
