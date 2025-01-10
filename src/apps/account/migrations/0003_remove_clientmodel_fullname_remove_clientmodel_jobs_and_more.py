# Generated by Django 4.2.6 on 2025-01-10 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_clientmodel_updated_at_alter_clientmodel_created_at_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clientmodel',
            name='fullname',
        ),
        migrations.RemoveField(
            model_name='clientmodel',
            name='jobs',
        ),
        migrations.AddField(
            model_name='clientmodel',
            name='password',
            field=models.CharField(default=1, max_length=150, verbose_name='Password'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='clientmodel',
            name='username',
            field=models.CharField(default=1, max_length=150, verbose_name='Username'),
            preserve_default=False,
        ),
    ]