from datetime import timedelta

from django.db import models
from django.db.models import TextChoices, Manager, CASCADE, SET_NULL, TextField, ForeignKey, URLField, DateTimeField, \
    ImageField, BooleanField, fields
from django.forms import CharField
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField

from apps.article.choise import Status
from apps.article.manager import PublishManager
from apps.shared.models import BaseModel


class Article(BaseModel):

    object = Manager()
    published = PublishManager()


    title = CharField(max_length=128)
    body = models.TextField()
    slug = models.SlugField(unique=True)
    published_at = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=15, choices=Status.choices, default=Status.DRAFT)
    category = models.ForeignKey('article.Category', CASCADE, 'articles')
    image = models.ImageField(upload_to='articles/images/')
    likes = models.IntegerField(default=0)
    owner = models.ForeignKey("account.Account", on_delete=SET_NULL, related_name='article', null=True)

class Category(BaseModel):
    name = CharField(max_length=128)

class Comment(BaseModel):
    body = TextField()
    owner = ForeignKey("account.Account", CASCADE, 'comments')
    article = ForeignKey("article.Article", CASCADE, 'comments')

def Advertisement_expire(*args, **kwargs):
    return timezone.now() + timedelta(days=3)


class Advertise(BaseModel):
    image = ImageField(upload_to='advertise/images/')
    url = URLField()
    phone = PhoneNumberField(region="UZ")
    expired_at = DateTimeField(default=Advertisement_expire)
    is_active = BooleanField(default=True)
