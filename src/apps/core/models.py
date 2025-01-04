from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField('Creation time', auto_now_add=True)
    updated_at = models.DateTimeField('Update time', auto_now=True)

    class Meta:
        abstract = True

    def get_created_at(self):
        return self.created_at.strftime('%Y-%m-%d %H:%M:%S')

    def get_created_date(self):
        return self.created_at.strftime('%Y-%m-%d')

