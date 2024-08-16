#Se importa el modulo de administración de Django.
from django.contrib import admin
#Se importa los modelos (mis tablas) desde el archivo actual.
from . models import Product, Perfil, Cart, Payment, OrderPlaced, Wishlist
#Se importa una función para formatear HTML de manera segura.
from django.utils.html import format_html
#Se importa una función para obtener la URL inversa de una vista.
from django.urls import reverse
#Se importa el modelo de grupo de Django, que luego se eliminará del panel de administración.
from django.contrib.auth.models import Group

# Register your models here.

""" 
Registro del modelo "Product":

1. ProductModelAdmin: Es una clase que define la configuración del modelo
"Product" en el panel de administración.
2. list_display: Es el que especifica los campos que se mostrarán en la lista
de productos en la interfaz de administración.
"""

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'discounted_price', 'category', 'product_image']


""" 
Registro del modelo "Perfil":

1. PerfilModelAdmin: Es una clase que define la configuración del modelo "Perfil"
en el panel de administración.
2. list_display: Es el que especifica los campos que se mostrarán en la lista
de productos en la interfaz de administración.

"""
    
@admin.register(Perfil)
class PerfilModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'localidad', 'ciudad', 'departamento']
    

""" 
Registro del modelo "Cart":

1. CartModelAdmin: Es una clase que define la configuración del modelo
"Cart" en el panel de administración.
2. list_display: Especifica los campos que se mostrarán en la lista de carritos 
en la interfaz de administración.
3. products: Es el método personalizado que genera un enlace a la página de 
administración del productp relacionado "format_html" se usa para crear un enlace
HTML seguro y "reverse" se usa para generar la URL de cambio del producto en la 
administración.

"""


@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'products', 'quantity']
    def products(self,obj):
        link = reverse("admin:app_product_change", args=[obj.product.pk])
        return format_html('<a href="{}">{}</a>', link, obj.product.title)
    
"""""
@admin.register(Payment)
class PaymentModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'amount', 'razorpay_order_id', 'razorpay_payment_status', 'razorpay_payment_id', 'paid']"""

"""""    
@admin.register(OrderPlaced)
class OrderPlacedModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'customer', 'product', 'quantity', 'ordered_date', 'status', 'payment']"""



""" 
Registro del modelo "Whislist":

1. WishlistModelAdmin: Es una clase que define la configuración del modelo
2. list_display: Especifica los campos que se mostrarán en la lista de listas de deseos
en la interfaz de administración.
3. products: Es el método personalizado que genera un enlace a la página de 
administración del producto relacionado. Similar al método en "CartModelAdmin".

"""

    
@admin.register(Wishlist)
class WishlistModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'products']
    def products(self,obj):
        link = reverse("admin:app_product_change", args=[obj.product.pk])
        return format_html('<a href="{}">{}</a>', link, obj.product.title)
    
""" 
Es el comando que elimina el modelo "Group" del panel de administración, lo que
significa que no estará disponible para su gestión a través de la interfaz de 
administración de Django.
"""

admin.site.unregister(Group)