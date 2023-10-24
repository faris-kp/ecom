from core.models import Product,Category,Vendor,ProductImages,CartOrderItems,CartOrder,ProductReview,Wishlist,Address

def custom_data(request):
    # Define a function that adds custom data to the context
    categories = Category.objects.all()
    
    return {
        'categories':categories,
    }