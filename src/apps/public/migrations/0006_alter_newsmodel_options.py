# Generated by Django 4.2.6 on 2025-01-06 17:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0005_newsmodel_remove_contactmodel_message_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='newsmodel',
            options={'verbose_name': 'News'},
        ),
    ]
