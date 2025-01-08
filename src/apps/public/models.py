from django.db import models
from ckeditor.fields import RichTextField
from apps.core.models import BaseModel

class NewsModel(BaseModel):
    title = models.CharField(max_length=250,verbose_name='News Title')
    content = RichTextField(verbose_name='Content News')
    class Meta:
        verbose_name = 'News'


class ContactModel(BaseModel):
    fullname = models.CharField(max_length=150,verbose_name='Full Name')
    job_title = models.CharField(max_length=150, verbose_name='Job Title')
    email = models.EmailField(unique=True,verbose_name='Email Address')
    is_read = models.BooleanField(default=False,verbose_name='Is_Read')

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'


class ArticleModel(BaseModel):
    title = models.CharField(max_length=200,verbose_name='Title Article')
    content = RichTextField(verbose_name='Content Article')
    summary = models.CharField(max_length=500,verbose_name='Summary')
    images = models.ImageField(upload_to='articles/images/',blank=True
                               ,null=True,verbose_name='Images')

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'


class AboutModel(models.Model):
    content = models.TextField(verbose_name='About Content')
    image_cover = models.ImageField(upload_to='about/images/',blank=True
                               ,null=True,verbose_name='Images')
    video = models.FileField(upload_to='about/videos/',blank=True,null=True
                             ,verbose_name='About Video')

    class Meta:
        verbose_name = 'About'


class ReviewModel(BaseModel):
    name = models.CharField(max_length=150, verbose_name='Name')
    feedback = models.TextField(verbose_name='Feedback')
    photo = models.ImageField(upload_to='reviews/photos/',blank=True,null=True,
                              verbose_name='Photo')
    video = models.FileField(upload_to='reviews/videos/',blank=True,null=True,
                             verbose_name='Video')

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'