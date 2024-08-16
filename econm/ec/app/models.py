""" 
Se importa el módulo de modelos de Django que se usa para defenir las 
estructuras de base de datos.
"""
from django.db import models
""" 
Se importa el modelo "User" del sistema de Django, para
crear relaciones entre los usuarios y otros modelos.
"""
from django.contrib.auth.models import User

# Create your models here.


""" 

'STATE_CHOICES' - 'CATEGORY_CHOICES':

Son tuplas de opciones que se usan en los campos de selección
en los modelos. Estos permiten al usuario seleccionar una 
opción predefinida de una lista.
"""

STATE_CHOICES = (
    ('San Salvador','San Salvador'),
    ('La Libertad','La Libertad'),
    ('San Miguel','San Miguel'),
    ('Santa Ana','Santa Ana'),
    ('Usulutan','Usulután'),
    ('Sonsonate','Sonsonate'),
    ('Ahuachapan','Ahuachapán'),
    ('La Paz','La Paz'),
    ('La Union','La Union'),
    ('San Vicente','San Vicente'),
    ('Chalatenango','Chalatenango'),
    ('Cuscatlan','Cuscutlán'),
    ('Morazan','Morazán'),
    ('Cabanas','Cabañas'),
)



CATEGORY_CHOICES = (
    ('PS', 'PlayStation 1'),
    ('PS', 'PlayStation 2'),
    ('PS', 'PlayStation 3'),
    ('PS', 'PlayStation 4'),
    ('PS', 'PlayStation 5'),
    
    #Las laptops
    ('PC', 'HP Victus 15'),
    ('PC', 'HP Victus 16'),
    ('PC', 'Lenovo Legion 5'),
    ('PC', 'ASUS TUF F15 GAMING'),
    ('PC', 'ASUS ROG G15'),
    
    #Los videojuegos
    ('G', 'Dark Soul'),
    ('G', 'God Of War 2'),
    ('G', 'God Of War 4'),
    ('G', 'Mass Effect 3'),
    ('G', 'Resident Evil 4 Remake'),
    ('G', 'Silent Hill'),
    ('G', 'Spiderman'),
    ('G', 'The Legend of Zelda: Breath of the Wild'),
    
    #Los mandos
    ('M', 'Mando para PlayStation 1'),
    ('M', 'Mando para PlayStation 2'),
    ('M', 'Mando para PlayStation 3'),
    ('M', 'Mando para PlayStation 4'),
    ('M', 'Mando para PlayStation 5'),   
)



""" 
    Mi tabla productos:
    
1. Product: Representa un producto en la tienda.
2. title: Es el nombre del producto.
3. selling_price: Es el precio de venta del producto.
4. discounted_price: Es el precio de venta del producto con descuento.
5. description: Es la descripción del producto.
6. category: Es la categoría del producto que viene de "CATEGORY_CHOICES".
7. product_image: Es la imagen del producto que se subirá al sistema.
8. __str__: Este método es usado para mostrar el nombre del producto en el administrador de Django.

"""
class Product(models.Model):
    title = models.CharField(max_length=255)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField()
    #prodapp = models.TextField(default='')
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    product_image = models.ImageField(upload_to='product')
    
    def __str__(self):
        return self.title
    

""" 
Mi tabla "Perfil":

1. Perfil: Representa un usuario en la tienda.
2. user: Es el usuario al que pertenece el perfil.
3. nombre: Es el nombre del usuario.
4. localidad: Es la localidad del usuario.
5. ciudad: Es la ciudad del usuario.
6. telefono: Es el número de teléfono del usuario.
7. departamento: Es el departamento del usuario que viene de "STATE_CHOICES".
8. __str__: Es el método que devuelve el nombre del perfil.

"""

class Perfil(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=255)
    localidad = models.CharField(max_length=255)
    ciudad = models.CharField(max_length=100)
    telefono = models.IntegerField()
    departamento = models.CharField(choices=STATE_CHOICES, max_length=100)
    
    def __str__(self):
        return self.nombre
    

""" 
Mi tabla "Targeta":

1. Targeta: Representa una tarjeta de compra.
2. user: Es la relación con el modelo "User" del usuario.
3. product: Es la relación con el modelo "Product" del producto.
4. quantity: Es la cantidad de productos en la tarjeta de compra.
5. total_cost: Es el método que calcula el costo total de la tarjeta de compra.
"""

class Targeta(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    
    @property
    def total_cost(self):
        return self.quantity * self.producto.discounted_price



STATUS_CHOICES = (
    
    ('Aceptado', 'Aceptado'),
    ('Lleno', 'Lleno'),
    ('En camino', 'En camino'),
    ('Entregado', 'Entregado'),
    ('Cancelar', 'Cancelar'),
    ('Pendiente', 'Pendiente'),
    
)


""" 
Mi tabla "Payment":

1. Payment: Representa un pago realizado del usuario.
2. user: Es la relación con el modelo "User" del usuario.
3. amount: Es la cantidad del pago.
4. razorpay_order_id, razor_payment_status, razor_payment_id: Son los
campos relacionados con la integración de pagos con Razorpay.
5. paid: Es el que indica si el pago ha sido realizado.
"""


class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.FloatField()
    razorpay_order_id = models.CharField(max_length=100, blank=True, null=True)
    razorpay_payment_status = models.CharField(max_length=100, blank=True, null=True)
    razorpay_payment_id = models.CharField(max_length=100, blank=True, null=True)
    paid = models.BooleanField(default=False)


""" 
Mi tabla "OrderPlaced":

1. OrderPlaced: Representa un pedido realizado por un usuario.
2. user: Es la relación con el modelo "User".
3. customer: Es la relación con el modelo "Perfil".
4. product: Es la relación con el modelo "Product".
5. quantity: Es la cantidad de productos en el pedido.
6. ordered_date: Es la fecha y hora en que el pedido fue realizado.
7. status: Es el estado del pedido que viene de "STATUS_CHOICES".
8. payment: Es la relación con el modelo "Payment".
9. total_cost: Es la propiedad que calcula el costo total del pedido.
"""

class OrderPlaced(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Perfil, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    ordered_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default='Pendiente')
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE, default="")
    
    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price
    

""" 
Mi tabla "Cart":

1. Cart: Representa un carrito de compra de un usuario.
2. user: Es la relación con el modelo "User".
3. product: Es la relación con el modelo "Product".
4. quantity: Es la cantidad de productos en el carrito.
"""
    
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)



""" 
Mi tabla "Wishlist":

1. Wishlist: Representa una lista de deseos de un usuario.
2. user: Es la relación con el modelo "User".
3. product: Es la relación con el modelo "Product".

"""

class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)