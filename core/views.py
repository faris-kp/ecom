from django.shortcuts import render
from core.models import Product,Category,Vendor,ProductImages,CartOrderItems,CartOrder,ProductReview,Wishlist,Address
# Create your views here.


def index(request):
    # products = Product.objects.all().order_by("-id")
    products = Product.objects.filter(product_status="published",featured=True)
    context ={
        "products":products
    }
    return render(request,'core/index.html',context)