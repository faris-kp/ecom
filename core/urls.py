from django.urls import path
from core import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("",views.index,name="index"),
    path("products/",views.product_list_view, name="products"),
    path("products/category/<cid>",views.category_product_list_view, name="category-list"),
    path("vendors/",views.vedor_list_view, name = "vendor-list")
]

if settings.DEBUG:
    
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


