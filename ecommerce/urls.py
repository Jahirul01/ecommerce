from django.conf.urls import url , include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from products.views import homepage

urlpatterns = [
      url(r'^admin/', admin.site.urls),
      url('', include('products.urls')),
      url('home',homepage,name='homepage')
]
if settings.DEBUG: # new
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

