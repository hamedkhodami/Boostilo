# Generated by Django 4.2.6 on 2025-01-08 12:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0005_rename_productmodel_portfoliomodel_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='portfoliomodel',
            options={'verbose_name': 'Portfolio', 'verbose_name_plural': 'Portfolios'},
        ),
    ]
