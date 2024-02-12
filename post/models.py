from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from tinymce.models import HTMLField
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify
from .author import Author
from .category import Category



class Post(models.Model):
    # Choices for post status
    DRAFT = 'draft'
    PUBLISHED = 'published'
    STATUS_CHOICES = [
        (DRAFT, 'Draft'),
        (PUBLISHED, 'Published'),
    ]

    # Core fields for the Post model
    title = models.CharField(max_length=200, unique=True)
    meta_title = models.CharField(max_length=200, blank=True)
    meta_description = models.CharField(max_length=350, blank=True)
    slug = models.SlugField(unique=True, blank=True)
    image = models.ImageField(upload_to='img/')
    content = HTMLField()

    # Date and time fields
    published = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(blank=True, null=True)

    # Additional fields
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=DRAFT)
    categories = models.ManyToManyField(Category)
    tags = models.CharField(blank=True, max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    featured = models.BooleanField(default=False)
    visit_count = models.IntegerField(default=0)
    comments_enabled = models.BooleanField(default=True)

    # Manager for custom queries
    objects = models.Manager()

    def publish(self):
        """Change the status of the post to 'Published' and update the published timestamp."""
        self.status = self.PUBLISHED
        self.published = timezone.now()
        self.save()

    def __str__(self):
        """String representation of the Post."""
        return self.title

    def get_absolute_url(self):
        """Get the absolute URL for the post."""
        return f"/post/{self.slug}/"


@receiver(pre_save, sender=Post)
def pre_save_post_receiver(sender, instance, *args, **kwargs):
    """Signal receiver to generate a unique slug before saving the post."""
    if not instance.slug:
        instance.slug = create_unique_slug(instance)


def create_unique_slug(instance, new_slug=None):
    """Generate a unique slug for the post."""
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    existing_slugs = Post.objects.filter(slug=slug).exclude(id=instance.id).order_by("-id")
    if existing_slugs.exists():
        new_slug = f"{slug}-{existing_slugs.first().id}"
        return create_unique_slug(instance, new_slug=new_slug)
    return slug
