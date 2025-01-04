from .base import REDIS_CONFIG
import os


# Database (postgresql)
DATABASES = {
    "default": {
        'ENGINE': 'django.db.backends.postgresql',
        "NAME": os.getenv("DB_NAME"),
        "USER": os.getenv("DB_USER"),
        "PASSWORD": os.getenv("DB_PASSWORD"),
        "HOST": os.getenv("DB_HOST"),
        "PORT": os.getenv("DB_PORT"),
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
    'redis': {
        'host': REDIS_CONFIG['host'],
        'port': REDIS_CONFIG['port'],
        'db': 0,
    }
}
