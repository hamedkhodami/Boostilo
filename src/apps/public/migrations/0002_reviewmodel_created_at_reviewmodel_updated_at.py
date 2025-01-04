# Generated by Django 4.2.6 on 2025-01-03 09:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviewmodel',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Creation time'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reviewmodel',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Update time'),
        ),
    ]
