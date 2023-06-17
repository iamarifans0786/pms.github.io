from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib.auth import authenticate,login
from app1.models import electronic_items_earphones,electronic_items_mobiles,electronic_items_watch
# Create your views here.


def default(request):
   return HttpResponse("Project Run Sucssesfull")

#Login

def login_function(request):
   massage=""
   error=""
   if request.method == 'POST':
      username=request.POST.get('user')
      password=request.POST.get('pass')
      user=authenticate(username=username,password=password)
      if user:
         login(request,user)
         return HttpResponseRedirect('/dashboard')
      else:
         error="Invalid User.."  
   return render(request,'login.html',{
      'masssge':error
   })

#dasboard

def dasboard(request):
   if request.user.is_authenticated:
      earphones=electronic_items_earphones.objects.all()
      mobiles=electronic_items_mobiles.objects.all()
      watches=electronic_items_watch.objects.all()
      data={
         'earphone':earphones,
         'mobile':mobiles,
         'watch':watches
      }
      return render(request,'dasboard.html',data)
   return HttpResponseRedirect('/login')


# Add Product
def Add_Product(request):
   if request.method == 'POST':
      ProductName=request.POST.get('Pro_name')
      Description=request.POST.get('desc')
      Price=request.POST.get('price')
      Stock=request.POST.get('stock')
      Colour=request.POST.get('colour')
      Category=request.POST.get('category') 

      if Category == 'Earphone':
         Earphone_product=electronic_items_earphones.objects.create(
         product_name=ProductName,
         description=Description,
         price=Price,
         stocks=Stock,
         color=Colour
         )
         Earphone_product.save()
         return HttpResponseRedirect('/dashboard')

      elif Category == 'Mobile':
         Mobile_product=electronic_items_mobiles.objects.create(
         product_name=ProductName,
         description=Description,
         price=Price,
         stocks=Stock,
         color=Colour
         )
         Mobile_product.save() 
         return HttpResponseRedirect('/dashboard')


      elif Category == 'Watch':
         Watch_product=electronic_items_watch.objects.create(
         product_name=ProductName,
         description=Description,
         price=Price,
         stocks=Stock,
         color=Colour
         )
         Watch_product.save() 
         return HttpResponseRedirect('/dashboard')   

   return render(request,'add-product.html')


# Product List

def product_list(request):
   earphones=electronic_items_earphones.objects.all()
   mobiles=electronic_items_mobiles.objects.all()
   watches=electronic_items_watch.objects.all()
   data={
      'earphone':earphones,
      'mobile':mobiles,
      'watch':watches
   }
   return render(request,'product-list.html',data)

# Edit - Product

def edit_product_earphones(request,id):
   product=electronic_items_earphones.objects.get(id=id)
   data={
      'product':product
   }
   if request.method=="POST":
      pro_name=request.POST.get("Pro_name")
      desc=request.POST.get("desc")
      price=request.POST.get("price")
      stock=request.POST.get("stock")
      colour=request.POST.get("colour")

      items=electronic_items_earphones.objects.get(id=id)
      items.product_name=pro_name
      items.description=desc
      items.price=price
      items.stocks=stock
      items.color=colour
      items.save()    
      return HttpResponseRedirect('/dashboard')  
   return render(request,'edit-product.html',data)

def edit_product_phones(request,id):
   product=electronic_items_mobiles.objects.get(id=id)
   data={
      'product':product
   }
   if request.method=="POST":
      pro_name=request.POST.get("Pro_name")
      desc=request.POST.get("desc")
      price=request.POST.get("price")
      stock=request.POST.get("stock")
      colour=request.POST.get("colour")

      items=electronic_items_mobiles.objects.get(id=id)
      items.product_name=pro_name
      items.description=desc
      items.price=price
      items.stocks=stock
      items.color=colour
      items.save()    
      return HttpResponseRedirect('/dashboard')  
   return render(request,'edit-product.html',data)

def edit_product_watches(request,id):
   product=electronic_items_watch.objects.get(id=id)
   data={
      'product':product
   }
   if request.method=="POST":
      pro_name=request.POST.get("Pro_name")
      desc=request.POST.get("desc")
      price=request.POST.get("price")
      stock=request.POST.get("stock")
      colour=request.POST.get("colour")

      items=electronic_items_watch.objects.get(id=id)
      items.product_name=pro_name
      items.description=desc
      items.price=price
      items.stocks=stock
      items.color=colour
      items.save()    
      return HttpResponseRedirect('/dashboard')  
   return render(request,'edit-product.html',data)



def delete_earphones(request,id):
   product=electronic_items_earphones.objects.get(id=id)
   if product:
      product.delete()
      return HttpResponseRedirect('/dashboard')  
   return render(request,'edit-product.html')

def delete_mobiles(request,id):
   product=electronic_items_mobiles.objects.get(id=id)
   if product:
      product.delete()
      return HttpResponseRedirect('/dashboard')  
   return render(request,'edit-product.html')

def delete_watches(request,id):
   product=electronic_items_watch.objects.get(id=id)
   if product:
      product.delete()
      return HttpResponseRedirect('/dashboard')  
   return render(request,'edit-product.html')