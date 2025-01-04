# Generated by Django 4.2.6 on 2025-01-02 18:53

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='About Content')),
                ('video', models.FileField(blank=True, null=True, upload_to='about/videos/', verbose_name='About Video')),
            ],
            options={
                'verbose_name': 'About',
            },
        ),
        migrations.CreateModel(
            name='ArticleModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Creation time')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Update time')),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('content', ckeditor.fields.RichTextField(verbose_name='Content')),
                ('summary', models.CharField(max_length=250, verbose_name='Summary')),
            ],
            options={
                'verbose_name': 'Article',
                'verbose_name_plural': 'Articles',
            },
        ),
        migrations.CreateModel(
            name='ContactModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=150, verbose_name='Full Name')),
                ('job_title', models.CharField(max_length=150, verbose_name='Job Title')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email Address')),
                ('message', models.TextField(verbose_name='Message')),
                ('is_read', models.BooleanField(default=False, verbose_name='Is_Read')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Creation Date')),
            ],
            options={
                'verbose_name': 'Contact',
                'verbose_name_plural': 'Contacts',
            },
        ),
        migrations.CreateModel(
            name='ReviewModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Name')),
                ('feedback', models.TextField(verbose_name='Feedback')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='reviews/photos/', verbose_name='Photo')),
                ('video', models.FileField(blank=True, null=True, upload_to='reviews/videos/', verbose_name='Video')),
            ],
            options={
                'verbose_name': 'Review',
                'verbose_name_plural': 'Reviews',
            },
        ),
        migrations.CreateModel(
            name='ArticleImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(blank=True, null=True, upload_to='articles/images/', verbose_name='Images')),
                ('caption', models.CharField(blank=True, max_length=200, null=True, verbose_name='Caption')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='image', to='public.articlemodel')),
            ],
            options={
                'verbose_name': 'Article Image',
                'verbose_name_plural': 'Articles Images',
            },
        ),
    ]