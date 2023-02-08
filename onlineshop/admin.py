from django.contrib import admin
from . models import *

# Register your models here.
@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display= ('id','user','name','locality', 'city', 'zipcode')

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display= ('id','name','company','price','original_price', 'description', 'image')

@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display= ('id','user','product', 'quantity')

@admin.register(OrderPlaced)
class OrderPlacedModelAdmin(admin.ModelAdmin):
    list_display= ('order_id','user','customer','product', 'quantity','order_date','status')

@admin.register(TestDrive)
class TestDriveAdmin(admin.ModelAdmin):
    list_display= ('id','name', 'email','phone' ,'bikemodel', 'address','zipcode', 'question')

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'email', 'phone', 'sub', 'question')