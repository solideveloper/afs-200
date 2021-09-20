from django.contrib import admin
from django.urls import include, path

from solipages.views import home_view, contact_view, about_view, blog_view


urlpatterns = [
    path('soliblog/', blog_view, name='soliblog'),
    path('solicourses/', include('solicourses.urls'), name='solicourses'),
    path('soliproducts/', include('soliproducts.urls'), name='soliproducts'),
    path('', home_view, name='home'),
    path('about/soliproducts/<int:id>/', about_view, name='product-detail'),
    path('contact/', contact_view, name='contact'),
    path('admin/', admin.site.urls, name='admin'),
]
