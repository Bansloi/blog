from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=200, null=True)
    slug = models.SlugField(unique=True, blank=True)
    image = models.CharField(max_length=300, null=True, blank=True)
    description = models.CharField(max_length=500, null=True, blank=True, verbose_name='Description')


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f"/category/{self.slug}/"  

@receiver(pre_save, sender=Category)
def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)

def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    existing_slugs = Category.objects.filter(slug=slug).exclude(id=instance.id).order_by("-id")
    if existing_slugs.exists():
        new_slug = f"{slug}-{existing_slugs.first().id}"
        return create_slug(instance, new_slug=new_slug)
    return slug


  