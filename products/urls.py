from django.conf.urls import url , include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from products.views import displayproduct
from products.views import detailsview
from products.views import *
from products.views import homepage

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    # url('', include('products.urls')),
    # url('homepage',homepage, name = 'homepage'),
    # url('displayproduct',displayproduct, name = 'displayproduct'),
    url(r'^$', displayproduct, name='displayproduct'), # set as homepage
    url(r'^detailsview/(?P<id>\d+)$', detailsview,name = 'detailsview'),
    url(r'^custommer_order/(?P<id>\d+)$', custommer_order,name = 'custommer_order'),
    url(r'^customer_order_submit/(?P<id>\d+)$',customer_order_submit,name='customer_order_submit'),
    # url(r'^$', homepage, name='homepage'), # set as homepage
    url('customer_order_view',customer_order_view,name = 'customer_order_view'),
]