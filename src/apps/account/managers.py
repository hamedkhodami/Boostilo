from django.db import models

class ActiveUserManager(models.Manager):
    def active_users(self):
        return self.filter(is_active=True)

    def admin_users(self):
        return self.filter(profile__role="admin")
