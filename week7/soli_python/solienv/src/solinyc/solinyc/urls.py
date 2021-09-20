from django.contrib import admin
from django.urls import include, path

from solipages.views import home_view, contact_view, about_view, blog_view


urlpatterns = [
    path('soliblog/', include('soliblog.urls')),
    path('solicourses/', include('solicourses.urls')),
    path('soliproducts/', include('soliproducts.urls')),
    path('', home_view, name='home'),
    path('about/<int:id>/', about_view, name='product-detail'),
    path('contact/', contact_view),
    path('admin/', admin.site.urls),
]
