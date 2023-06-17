from django.contrib import admin
from app1.models import electronic_items_earphones,electronic_items_mobiles,electronic_items_watch

# Register your models here.

class Edit_electronic_items_earphones(admin.ModelAdmin):
   list_display=[
      'product_name',
      'description',
      'price',
      'stocks',
      'color',
   ]
   search_fields=[
       'product_name',
   ]
   list_filter=[
      'price',
      'color',
   ]

admin.site.register(electronic_items_earphones,Edit_electronic_items_earphones)


class Edit_electronic_items_mobiles(admin.ModelAdmin):
   list_display=[
      'product_name',
      'description',
      'price',
      'stocks',
      'color',
   ]
   search_fields=[
       'product_name',
   ]
   list_filter=[
      'price',
      'color',
   ]


admin.site.register(electronic_items_mobiles,Edit_electronic_items_mobiles)

class Edit_electronic_items_watch(admin.ModelAdmin):
   list_display=[
      'product_name',
      'description',
      'price',
      'stocks',
      'color',
   ]
   search_fields=[
       'product_name',
   ]
   list_filter=[
      'price',
      'color',
   ]
 

admin.site.register(electronic_items_watch,Edit_electronic_items_watch)

