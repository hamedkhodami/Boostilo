# Generated by Django 4.2.6 on 2025-01-02 07:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=150, verbose_name='Full Name')),
                ('jobs', models.CharField(max_length=150, verbose_name='Job Title')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email Address')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Creation Date')),
            ],
            options={
                'verbose_name': 'Client',
                'verbose_name_plural': 'Clients',
            },
        ),
        migrations.CreateModel(
            name='ProfileTeam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Creation time')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Update time')),
                ('fullname', models.CharField(max_length=50, verbose_name='Full Name')),
                ('role', models.CharField(choices=[('admin', 'Admin'), ('team', 'Team_member')], max_length=150, verbose_name='Role')),
                ('bio', models.TextField(verbose_name='Biography')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='images/profiles/', verbose_name='Profile Photo')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Profile',
                'verbose_name_plural': 'Profiles',
            },
        ),
        migrations.CreateModel(
            name='AccessControl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active Status')),
                ('can_edit', models.BooleanField(default=False, verbose_name='Can Edit Content')),
                ('can_delete', models.BooleanField(default=False, verbose_name='Can Delete Content')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='Superuser Status')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='access_control', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Access Control',
                'verbose_name_plural': 'Access Controls',
            },
        ),
    ]
