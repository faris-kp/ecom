from core.models import Product,Category,Vendor,ProductImages,CartOrderItems,CartOrder,ProductReview,Wishlist,Address
from django.db.models import Count
def custom_data(request):
    # Define a function that adds custom data to the context
    categories_with_product_count = Category.objects.annotate(product_count=Count('category'))
    # categories = Category.objects.all()
    categories = categories_with_product_count.filter(product_count__gt=0)
    
    
    
    vendor_with_product_count = Vendor.objects.annotate(product_count=Count('vendor'))
    vendors = vendor_with_product_count.filter(product_count__gt=0)
    
    
    return {
        'categories':categories,
        'vendors':vendors
    }