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