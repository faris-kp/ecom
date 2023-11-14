from django.urls import path
from core import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("",views.index,name="index"),
    #product
    path("products/",views.product_list_view, name="products"),
    path("products/category/<cid>",views.category_product_list_view, name="category-list"),
    path("products/<pid>",views.product_detail_view, name="product-detail"),
    path("filter-product/",views.filter_product,name="filter-product"),
    path("add-to-cart/", views.add_to_cart, name="add-to-cart"),
    
    #vendors
    path("vendors/",views.vendor_list_view, name = "vendor-list"),
    path("vendors/<vid>",views.vendor_detail_view, name = "vendor-detail"),
    
    
    # tags
    
    path("prodcuts/tag/<slug:tag_slug>",views.tag_list, name="tags"),
    path("search/",views.serch_veiw,name="search"),
    
    
]

if settings.DEBUG:
    
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


