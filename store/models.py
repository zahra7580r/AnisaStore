from django.db import models
from uuid import uuid4
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

UserModel = get_user_model()


# Create your models here.

class BaseObject(models.Model):
    uuid = models.UUIDField(default=uuid4, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(UserModel, on_delete=models.PROTECT, related_name='%(app_label)s_%(class)s_touser')
    mod_user = models.ForeignKey(UserModel, on_delete=models.PROTECT, related_name='%(app_label)s_%(class)s_tomoduser')

    class Meta:
        abstract = True


class Book(BaseObject):
    title = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField(null=True, blank=True)
    author = models.ForeignKey('Author', on_delete=models.PROTECT)
    year = models.IntegerField()
    rank = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.title} ({self.year})"


class Author(BaseObject):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
