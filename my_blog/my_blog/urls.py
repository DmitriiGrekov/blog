from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.sitemaps.views import sitemap
from blog.sitemaps import ArticleSitemap

sitemaps = {
        'posts':ArticleSitemap,
        }

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('blog.urls',namespace='blog')),
    path('sitemap.xml',sitemap,{'sitemaps':sitemaps}),
    path('services/',include('services.urls',namespace = 'service')),
    path('questions/',include('questions.urls',namespace='questions')),
    path('books/',include('books_app.urls',namespace='books_app')),
    path('auth/',include('django.contrib.auth.urls')),
    path('accounts/',include('accounts.urls')),

    
    
    ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
