# Generated by Django 4.2.6 on 2025-01-03 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0002_reviewmodel_created_at_reviewmodel_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactmodel',
            name='message',
            field=models.TextField(max_length=500, verbose_name='Message'),
        ),
    ]