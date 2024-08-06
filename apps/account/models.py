from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import CharField, BooleanField, TextField, ForeignKey, URLField, CASCADE

from apps.account.choices import AccountRole
from apps.shared.models import BaseModel


class Account(BaseModel, AbstractUser):
    role = CharField(max_length=128, choices=AccountRole.choices, default=AccountRole.MEMBER)
    is_subscribe = BooleanField(default=False)

class Feed(BaseModel):
    name = CharField(max_length=128)
    body = TextField()
    website = URLField(null=True, blank=True)
    owner = ForeignKey("account.Account", CASCADE, related_name="feeds")

class Blog(BaseModel):
    title = models.CharField(max_length=128)
    body = models.TextField()
    image = models.ImageField(upload_to='blog/images/')
    customer = models.ForeignKey("account.Account", CASCADE, related_name="blogs")
