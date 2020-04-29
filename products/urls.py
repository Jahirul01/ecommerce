from django.conf.urls import url , include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from products.views import displayproduct
from products.views import homepage

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    # url('', include('products.urls')),
    # url('homepage',homepage, name = 'homepage'),
    url('displayproduct',displayproduct, name = 'displayproduct'),
    url(r'^$', homepage, name='homepage'), # set as homepage
]