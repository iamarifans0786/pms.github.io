from django.contrib import admin
from django.urls import path
from app1 import views

urlpatterns = [
   path("",views.default),
   path("login/",views.login_function, name="login"),
   path("dashboard/",views.dasboard, name="dashboard"),
   path("add-product/",views.Add_Product, name="add_product"),
   path("product-list/",views.product_list, name="product_list"),
   path("edit-earphones/<id>",views.edit_product_earphones, name="earphone_edit"),
   path("edit-mobiles/<id>",views.edit_product_phones, name="mobile_edit"),
   path("edit-watches/<id>",views.edit_product_watches, name="watch_edit"),
   path("del-earphones/<id>",views.delete_earphones, name="earphone_del"),
   path("del-mobiles/<id>",views.delete_mobiles, name="mobile_del"),
   path("del-watches/<id>",views.delete_watches, name="watches_del"),

]
