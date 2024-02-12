# manager.py

from django.db import models
from django.utils.text import slugify

class PostManager(models.Manager):
    def create_slug(self, instance, new_slug=None):
        slug = slugify(instance.title)
        if new_slug is not None:
            slug = new_slug
        existing_slugs = self.filter(slug=slug).exclude(id=instance.id).order_by("-id")
        if existing_slugs.exists():
            new_slug = f"{slug}-{existing_slugs.first().id}"
            return self.create_slug(instance, new_slug=new_slug)
        return slug
