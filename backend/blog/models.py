from django.db import models
from django.conf import settings


class Profile(models.Model):
    user = models.one_to_one_field(settings.AUTH_USER_MODEL,
            on_delete=models.CASCADE)
    website = models.URLField(blank=True)
    bio = models.CharField(max_length=264, blank=True)

    def __str__(self) -> str:
        return self.user.get_username()


class Tag(models.Model):
    name = models.CharField(max_length=150, unique=True)

    def __str__(self) -> str:
        return self.name


class Post(models.Model):

    class meta:
        ordering = ["publish_date"]
    
    title = models.CharField(max_length=255, blank=True)
    subtitle = models.CharField(max_length=255, blank=True)
    slug= models.SlugField(max_length=255, blank=True)
    body = models.TextField()
    meta_description = models.CharField(max_length=150, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    publish_date = models.DateTimeField(blank=True, null=True)
    published = models.BooleanField(default=False)
    author = models.ForeignKey(Profile, on_delete=models.PROTECT)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self) -> str:
        return self.title


