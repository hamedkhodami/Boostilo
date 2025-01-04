from .base import BASE_DIR
import os

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.getenv('SQLITE_PATH', BASE_DIR / 'db.sqlite3'),
    }
}

# Django-q config
Q_CLUSTER = {
    'name': 'django-q',
    'workers': int(os.getenv('Q_CLUSTER_WORKERS', 4)),
    'recycle': int(os.getenv('Q_CLUSTER_RECYCLE', 500)),
    'timeout': int(os.getenv('Q_CLUSTER_TIMEOUT', 60)),
    'compress': True,
    'queue_limit': 500,
    'orm': 'default',
}
