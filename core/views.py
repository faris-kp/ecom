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



def product_list_view(request):
    products = Product.objects.filter(product_status="published")
    context ={
        "products":products
    }
    return render(request,'core/product-list.html',context)


def category_product_list_view(request,cid):
    
    category = Category.objects.get(cid=cid)
    # print("category cheiking",category)
    # products = Product.objects.all().order_by("-id")
    products = Product.objects.filter(product_status="published",Category=category)
    
    context ={
        "category":category,
        "Products":products
    }
    return render(request,'core/category-product-list.html',context)

def vedor_list_view(request):
    vendor = Vendor.objects.all()
    
    context = {
        "vendors":vendor
    }
    return render(request,'core/vendor-list.html',context)