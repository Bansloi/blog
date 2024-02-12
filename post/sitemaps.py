from django.contrib.sitemaps import Sitemap
from .models import Post





class PostSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        return Post.objects.all().order_by("-published")

    def lastmod(self, obj):
        return obj.updated
