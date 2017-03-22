from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$', views.index, name='index' ),
    url(r'^(?P<category_slug>[-\w]+)/$', views.index, name='index_category'),
    url(r'^(?P<product_id>\d+)/(?P<product_slug>[-\w]+)/$',views.product_detail, name='product_detail'),
]