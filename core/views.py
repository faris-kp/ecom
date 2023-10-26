from django.shortcuts import render
from django.db.models import Count
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
    print("product cheking",products)
    context ={
        "products":products
    }
    return render(request,'core/product-list.html',context)


def product_detail_view(request,pid):
    product = Product.objects.get(pid=pid)
    p_image = product.p_images.all()
    address = Address.objects.get(user=request.user)
    
    context = {
        "product":product,
        "p_image":p_image,
        "addr":address
    }
    
    return render(request,"core/product-detail.html",context)

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

def vendor_list_view(request):
    vendor = Vendor.objects.all()
    
    context = {
        "vendors":vendor
    }
    return render(request,'core/vendor-list.html',context)

def vendor_detail_view(request,vid):
    vendor = Vendor.objects.get(Vid=vid)
    products_for_vendor = Product.objects.filter(vendor__Vid=vid)
    # print("vend_cat_chek",products_for_vendor)
    categories_for_vendor = products_for_vendor.values_list('Category__cid','Category__title',).distinct()
    products = Product.objects.filter(vendor=vendor,product_status="published")
    # print("cat_cat_chek",categories_for_vendor)
    context = {
        "vendors":vendor,
        "cat":categories_for_vendor,
        "products":products
        # "cat":categories_with_products
    }
    return render(request,'core/vendor-detail.html',context)

