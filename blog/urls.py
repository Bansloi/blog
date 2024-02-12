from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from post.sitemaps import PostSitemap
from django.contrib.sitemaps.views import sitemap
from django.views.generic import RedirectView

sitemaps = {
    "posts": PostSitemap,
}


urlpatterns = [
    path('admin/', admin.site.urls),
    path('favicon.ico/',RedirectView.as_view(url='/static/favicon/favicon.ico')),
    path('', include('post.urls')),
    path('tinymce/', include('tinymce.urls')),
    path('robots.txt/', include('robots.urls')),
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
