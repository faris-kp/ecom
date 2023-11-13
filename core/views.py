from django.shortcuts import render, get_object_or_404
from django.db.models import Count
from taggit.models import Tag
from core.models import Product,Category,Vendor,ProductImages,CartOrderItems,CartOrder,ProductReview,Wishlist,Address
from django.template.loader import render_to_string
from django.http import JsonResponse
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
        "products":products,
    }
    return render(request,'core/product-list.html',context)


def product_detail_view(request,pid):
    product = Product.objects.get(pid=pid)
    p_image = product.p_images.all()
    address = Address.objects.get(user=request.user)
    products = Product.objects.filter(Category=product.Category).exclude(pid=pid)
    # whatever product category in .here we show all prodcut with same category.excluding the same product that showing in deatail page
    #we can also use e[:4] for first 4 product
    print("catprop,",products)
    context = {
        "product":product,
        "p_image":p_image,
        "addr":address,
        "cat_products":products
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



def tag_list(request,tag_slug=None):
    products = Product.objects.filter(product_status="published").order_by("-id")
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        products = products.filter(tags__in=[tag])
        
    
    context = {
        "products":products,
        "tag":tag
    }
    
    return render(request,"core/tag.html", context)

def serch_veiw(request):
    query = request.GET.get("q")
    print("ueef",query)
    all = Product.objects.filter(product_status="published")
    print("all",all)
    products = Product.objects.filter(title__icontains=query).order_by("-date")
    print("search cheking",products)
    if not products.exists():
        print("Function Entered")
        context = {
        "Products": all,
        "query": "All Products"
    }
    else:
        print("Else function entered")
        context = {
        "Products": products,
        "query": query
    }

    print("context cheking",context)
    
    return render(request,"core/search.html",context)
    
    

def filter_product(request):
    categories = request.GET.getlist("category[]")
    vendors = request.GET.getlist("vendor[]")
    min_price = request.GET['min_price']
    max_price = request.GET['max_price']
    print("minprice =",min_price)
    print("max_price=",max_price)
    
    products = Product.objects.filter(product_status="published").order_by("-id").distinct()
    
    products =products.filter(price__gte =min_price,price__lte =max_price )
    print("minprice pr =",products)
    products =products.filter()
    print("maxnprice pr =",products)
    
    if len(categories) > 0:
        products = products.filter(Category__id__in=categories).distinct()
        
    if len(vendors) > 0:
        products = products.filter(vendor__id__in=vendors).distinct()
        print("vendor cheking",products)
        
    print("products after addingmin max=",products)
    data = render_to_string("core/async/product-list.html",{"products":products})
    
    
    return JsonResponse({"data":data})