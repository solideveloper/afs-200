"""solinyc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from solipages import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import include, path
from solisite.views import home_view, contact_view, about_view, blog_view, aboutProduct_view
from soliproducts.views import product_list_view
from solicourses.views import CourseListView
from members.views import login_user, register_user

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', home_view, name='home'),
    path('members/', include('members.urls'), name="login_user"),
    path('members/', include('django.contrib.auth.urls')),
    
    path('soliproducts/', include('soliproducts.urls'), name='soliproducts'),
    path('about/soliproducts/<int:id>/', aboutProduct_view, name='product-detail'),
    path('soliproducts/', product_list_view, name='about'),
    
    path('contact/', contact_view, name='contact'),
    path('soliblog/', blog_view, name='soliblog'),
    
    path('solicourses/', include('solicourses.urls'), name='solicourses'),
    path('courses/solicourses/<int:id>/', CourseListView, name='CourseListView'),
    path('solicourses/', CourseListView, name='courses'),
]