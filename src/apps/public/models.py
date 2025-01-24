from django.db import models
from ckeditor.fields import RichTextField
from apps.core.models import BaseModel

from .tasks import send_notif_to_admins


class NewsModel(BaseModel):
    title = models.CharField(max_length=250, verbose_name='News Title')
    content = RichTextField(verbose_name='Content News')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'


class ContactModel(BaseModel):
    fullname = models.CharField(max_length=150, verbose_name='Full Name')
    email = models.EmailField(unique=True, verbose_name='Email Address')
    is_read = models.BooleanField(default=False, verbose_name='Is_Read')

    def __str__(self):
        return self.fullname

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # senf notif
        send_notif_to_admins(self.fullname, self.email)


class ArticleModel(BaseModel):
    title = models.CharField(max_length=200, verbose_name='Title Article')
    content = RichTextField(verbose_name='Content Article')
    summary = models.CharField(max_length=500, verbose_name='Summary')
    images = models.ImageField(upload_to='articles/images/', blank=True
                               , null=True, verbose_name='Images')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

    def get_image(self):
        if self.images:
            return self.images.url
        return '/static/assets/public/images/logo.png' # TODO: should change image



class AboutModel(models.Model):
    content = models.TextField(verbose_name='About Content')
    image_cover = models.ImageField(upload_to='about/images/', blank=True
                                    , null=True, verbose_name='Images')
    video = models.FileField(upload_to='about/videos/', blank=True, null=True
                             , verbose_name='About Video')

    class Meta:
        verbose_name = 'About'


class ReviewModel(BaseModel):
    name = models.CharField(max_length=150, verbose_name='Name')
    feedback = models.TextField(verbose_name='Feedback')
    photo = models.ImageField(upload_to='reviews/photos/', blank=True, null=True,
                              verbose_name='Photo')
    video = models.FileField(upload_to='reviews/videos/', blank=True, null=True,
                             verbose_name='Video')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'

    def get_image(self):
        if self.photo:
            return self.photo.url
        return '/static/assets/public/images/logo.png' # TODO: should change image


