from pathlib import Path
import os

from ckeditor_demo.settings import CKEDITOR_UPLOAD_PATH
from django.conf.global_settings import AUTH_USER_MODEL, AUTHENTICATION_BACKENDS, EMAIL_HOST, EMAIL_PORT, \
    EMAIL_HOST_PASSWORD, EMAIL_USE_TLS, EMAIL_BACKEND
from dotenv import load_dotenv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent


#---ENV-------------------------------------------------------------
load_dotenv(dotenv_path=BASE_DIR / '.env')
#----------------------------------------------------------------



#---SECURITY------------------------------------------------------
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')

DEBUG = True

ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '*').split(',')
#----------------------------------------------------------------


#---CSRF---------------------------------------------------------
CSRF_TRUSTED_ORIGINS = os.getenv('CSRF_TRUSTED', 'http://127.0.0.1',).split(',')
#----------------------------------------------------------------


#---Application definition---------------------------------------

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    #apps
    'apps.core.apps.CoreConfig',
    'apps.account.apps.AccountConfig',
    'apps.public.apps.PublicConfig',
    'apps.service.apps.ServiceConfig',

    # Django modules
    'django_q',
    'ckeditor',
    'ckeditor_uploader',
    'smart_selects',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },

    },
]

WSGI_APPLICATION = 'config.wsgi.application'
#----------------------------------------------------------------


#---Password validation-------------------------------------------------------------
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]
#----------------------------------------------------------------


#---Internationalization------------------------------------------
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True
#----------------------------------------------------------------


#---Static files-------------------------------------------------

STATIC_URL = '/static/'
STATIC_ROOT = os.getenv('STATIC_ROOT')

STATICFILES_DIRS = [
   os.getenv('STATICFILES_DIRS', BASE_DIR / 'static/assets/'),
]
#----------------------------------------------------------------


#---Media--------------------------------------------------------
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / os.getenv('MEDIA_ROOT', 'static/media')
#----------------------------------------------------------------


#---Production whitenoise----------------------------------------
if int(os.getenv('ENABLE_WHITENOISE', default=0)):
    # Insert Whitenoise Middleware and set as StaticFileStorage
    MIDDLEWARE += [
        'whitenoise.middleware.WhiteNoiseMiddleware',
    ]
    STATICFILES_STORAGE = 'whitenoise.storage.StaticFilesStorage'
#----------------------------------------------------------------



#---REDIS--------------------------------------------------------
REDIS_CONFIG = {
    'active': int(os.getenv('REDIS_ACTIVE', 0)),  # 1 redis is connected, 0 not connected
    'host': os.getenv('REDIS_HOST', 'localhost'),
    'port': int(os.getenv('REDIS_PORT', 6379))
}
#----------------------------------------------------------------


#---CKEDITOR-----------------------------------------------------
CKEDITOR_UPLOAD_PATH = 'uploads/'
CKEDITOR_IMAGE_BACKEND = "pillow"
CKEDITOR_JQUERY_URL = '//ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js'
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
        'width': 'auto',
        'extraPlugins': ','.join([
            'codesnippet',
            'image2',
            'colorbutton',
        ]),
        'filebrowserUploadUrl': '/ckeditor/upload/',
        'filebrowserBrowseUrl': '/ckeditor/browse/',
        'toolbar': [
            { 'name': 'document', 'items': ['Source', '-', 'Save', 'NewPage', 'Preview', 'Print', '-', 'Templates' ] },
            { 'name': 'clipboard', 'items': [ 'Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'Undo', 'Redo' ] },
            { 'name': 'editing', 'items': [ 'Find', 'Replace', '-', 'SelectAll', '-', 'Scayt' ] },
            { 'name': 'basicstyles', 'items': [ 'Bold', 'Italic', 'Underline', 'Strike', '-', 'RemoveFormat' ] },
            { 'name': 'paragraph', 'items': [ 'NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote', 'CreateDiv', '-', 'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock', '-', 'BidiLtr', 'BidiRtl' ] },
            { 'name': 'links', 'items': [ 'Link', 'Unlink', 'Anchor' ] },
            { 'name': 'insert', 'items': [ 'Image', 'Table', 'HorizontalRule', 'SpecialChar', 'PageBreak', 'Iframe' ] },
            { 'name': 'styles', 'items': [ 'Styles', 'Format', 'Font', 'FontSize' ] },
            { 'name': 'colors', 'items': [ 'TextColor', 'BGColor' ] },
            { 'name': 'tools', 'items': [ 'Maximize', 'ShowBlocks' ] },
        ],
    },
}
#----------------------------------------------------------------


#---AUTHENTICATION------------------------------------------------
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'apps.account.backends.EmailBackend',
]
#----------------------------------------------------------------


#---EMAIL--------------------------------------------------------
EMAIL_BACKEND = os.getenv('EMAIL_BACKEND')
EMAIL_HOST = os.getenv('EMAIL_HOST')
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
EMAIL_PORT = int(os.getenv('EMAIL_PORT', 587))
EMAIL_USE_TLS = os.getenv('EMAIL_USE_TLS') == 'True'
DEFAULT_FROM_EMAIL = os.getenv('DEFAULT_FROM_EMAIL')
#----------------------------------------------------------------

