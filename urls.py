"""wokshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path,include



#from django.contrib import admin
from product.views import product_view1,product_view2,product_view3,product_view4

urlpatterns = [

    path('product/', include('product.urls')),
    path('product1/', product_view1),
    path('product2/', product_view2),
    path('product3/', product_view3),
    path('product4/', product_view4),
   # path('admin/',admin.site.urls),
]

