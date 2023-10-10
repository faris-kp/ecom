from django.db import models
from shortuuid.django_fields import ShortUUIDField
from django.utils.html import mark_safe
from userauths.models import User

def user_directory_path(instance,filename):
    return 'user_{0}/{1}'.format(instance.user.id, filename)

class Category(models.Model):
    cid = ShortUUIDField(unique = True , length =10 , max_length = 20 ,prefix = "cat" ,alphabet ="abcdefgh12345")
    title = models.CharField(max_length=100,default="Food")
    image = models.ImageField(upload_to="category",default="category.jpg")
    
    class Meta:
        verbose_name_plural = "Categories"
        
    def category_image(self):
        return mark_safe('<img src="%s" width ="50" ,height="50" />' % (self.image.url))
    
    def __str__(self):
        return self.title
    
    
class Tags(models.Model):
    pass
    
class Vendor(models.model):
    Vid = ShortUUIDField(unique = True , length =10 , max_length = 20 ,prefix = "ven" ,alphabet ="abcdefgh12345")
    title = models.CharField(max_length=100,default="Nesto")
    image = models.ImageField(upload_to="category",default="vendor.jpg")
    decription  = models.TextField(null=True, blank=True, default="I am  an amazing vendor")
    
    address = models.CharField(max_length=200, default="123 Street Road")
    contact = models.CharField(max_length=100,default="+91-000000")
    chat_resp_time = models.CharField(max_length=100, default="100")
    shipping_on_time = models.CharField(max_length=100, default="100")
    authentic_rating = models.CharField(max_length=100, default="100")
    days_return= models.CharField(max_length=100, default="100")
    warranty_period = models.CharField(max_length=100, default="100")
    
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    
    
    
    class Meta:
        verbose_name_plural = "Vendors"
        
    def vendor_image(self):
        return mark_safe('<img src="%s" width ="50" ,height="50" />' % (self.image.url))
    
    def __str__(self):
        return self.title
    
    
class Product(models.Model):
    pid = ShortUUIDField(unique = True , length =10 , max_length = 20 ,prefix = "cat" ,alphabet ="abcdefgh12345")
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    Category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=100,default="Fresh")
    image = models.ImageField(upload_to="category",default="product.jpg")
    decription  = models.TextField(null=True, blank=True, default="This is the product")
    
    
    price = models.DecimalField(max_digits=9999999999,decimal_places=2, default="1.99")
    old_price = models.DecimalField(max_digits=9999999999,decimal_places=2, default="2.99")
    
    specification = models.TextField(null=True,blank=True)
    
    
    