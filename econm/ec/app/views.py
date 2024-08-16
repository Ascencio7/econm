#Se importa "re" para obtener expresiones de Python
import re
#Se importa "Count" para realizar agregaciones.
from django.db.models import Count
#Se importa "render y rederict" para rederigir a otras vistas de "hmtl" 
from django.shortcuts import render, redirect
#from urllib import request

#Se importa "View" para crear vistas basadas de mis clases.
from django.views import View
#import razorpay

#Se importa "settings" para obtener la configuración del proyecto
from django.conf import settings
#Se importan todas mi tablas de modelos que he creado.
from . models import OrderPlaced, Perfil, Product, Cart, Wishlist
#Se importan mis formularios personalizados desde "forms" de mi app.
from . forms import CustomerRegistrationForm, PerfilProfileForm
#Se importa "messages" para mostrar mensajes de Django a los usuarios.
from django.contrib import messages
#Se importa el formato "JSON" para devolver respuestas al usuario.
from django.http import JsonResponse
#Se importa "Q" para realizar consultas en los modelos de Django.
from django.db.models import Q
#Se importa "login_required" para restringir el acceso a las vistas a usuarios no autenticados y autenticados.
from django.contrib.auth.decorators import login_required

from django.utils.decorators import method_decorator
# Create your views here.

#@login_required
""" 
"home" recibirá toda la información de la solicitud "HTTP".
Se inician dos variables en 0  para almacenar el número de artículos en 
el carrito y la lista de deseos.
Después va a verificar si el usuario realizó la solicitud de login
"""
def home(request):
    totalitem = 0
    wishitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
        wishitem = len(Wishlist.objects.filter(user = request.user))
    return render(request, "app/home.html", locals())

@login_required
def about(request):
    totalitem = 0
    wishitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
        wishitem = len(Wishlist.objects.filter(user = request.user))
    return render(request, "app/about.html", locals())

@login_required
def contact(request):
    totalitem = 0
    wishitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
        wishitem = len(Wishlist.objects.filter(user = request.user))
    return render(request, "app/contact.html", locals())

@method_decorator(login_required, name='dispatch')
class CategoryView(View):
    def get(self, request, val):
        totalitem = 0
        wishitem = 0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
            wishitem = len(Wishlist.objects.filter(user = request.user))
        product = Product.objects.filter(category=val)
        title = Product.objects.filter(category=val).values('title')
        return render(request, "app/category.html", locals())

@method_decorator(login_required, name='dispatch')
class CategoryTitle(View):
    def get(self, request, val):
        product = Product.objects.filter(title=val)
        title = Product.objects.filter(category=product[0].category).values('title')
        totalitem = 0
        wishitem = 0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
            wishitem = len(Wishlist.objects.filter(user = request.user))
        return render(request, "app/category.html", locals())
    
@method_decorator(login_required, name='dispatch')
class ProductDetail(View):
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        totalitem = 0
        wishitem = 0
        wishlist = Wishlist.objects.filter(Q(product=product) & Q(user=request.user))
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
            wishitem = len(Wishlist.objects.filter(user = request.user))
        return render(request, "app/productdetail.html", locals())
    
    

class CustomerRegistrationView(View):
    def get(self, request):
        form = CustomerRegistrationForm()
        totalitem = 0
        wishitem = 0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
            wishitem = len(Wishlist.objects.filter(user = request.user))
        return render(request, "app/customerregistration.html", locals())
    def post(self, request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "  Usuario registrado correctamente en VLADI STORE")
        else:
            messages.warning(request, "Datos inválidos, revisa los campos del registro.")
        return render(request, "app/customerregistration.html", locals())


@method_decorator(login_required, name='dispatch')    
class ProfileView(View):
    def get(self, request):
        form = PerfilProfileForm()
        totalitem = 0
        wishitem = 0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
            wishitem = len(Wishlist.objects.filter(user = request.user))
        return render(request, 'app/profile.html', locals())
    def post(self, request):
        form = PerfilProfileForm(request.POST)
        if form.is_valid():
            user = request.user
            nombre = form.cleaned_data['nombre']
            localidad = form.cleaned_data['localidad']
            ciudad = form.cleaned_data['ciudad']
            telefono = form.cleaned_data['telefono']
            departamento = form.cleaned_data['departamento']
            
            reg = Perfil(user=user, nombre=nombre,localidad=localidad, ciudad=ciudad, telefono=telefono, departamento=departamento)
            reg.save()
            messages.success(request, "Perfil guardado correctamente")
        else:
            messages.warning(request, "Datos inválidos, revisa los campos del formulario.")
            
        return render(request, 'app/profile.html', locals())
    

@login_required
def address(request):
    add = Perfil.objects.filter(user=request.user)
    totalitem = 0
    wishitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
        wishitem = len(Wishlist.objects.filter(user = request.user))
    return render(request, 'app/address.html', locals())



@method_decorator(login_required, name='dispatch')
class updateAddress(View):
    def get(self, request, pk):
        add = Perfil.objects.get(pk=pk)
        form = PerfilProfileForm(instance=add)
        totalitem = 0
        wishitem = 0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
            wishitem = len(Wishlist.objects.filter(user = request.user))
        return render(request, 'app/updateAddress.html', locals())
    def post(self, request, pk):
        form = PerfilProfileForm(request.POST)
        if form.is_valid():
            add = Perfil.objects.get(pk=pk)
            add.nombre = form.cleaned_data['nombre']
            add.localidad = form.cleaned_data['localidad']
            add.ciudad = form.cleaned_data['ciudad']
            add.telefono = form.cleaned_data['telefono']
            add.departamento = form.cleaned_data['departamento']
            add.save()
            messages.success(request, "Perfil modificado correctamente.")
        else:
            messages.warning(request, "Datos inválidos, revisa los campos del formulario.")
        return render(request, 'app/updateAddress.html', locals())
    

@login_required
def add_to_cart(request):
    user = request.user
    product_id = request.GET.get('prod_id')
    product = Product.objects.get(id=product_id)
    Cart(user=user, product=product).save()
    return redirect("/cart")


@login_required
def show_cart(request):
    user = request.user
    cart = Cart.objects.filter(user=user)
    amount = 0
    for p in cart:
        value = p.quantity * p.product.discounted_price
        amount = amount + value
    totalamount = amount + 40
    totalitem = 0
    wishitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
        wishitem = len(Wishlist.objects.filter(user = request.user))
    return render(request, 'app/addtocart.html', locals())


@method_decorator(login_required, name='dispatch')
class checkout(View):
    def get(self, request):
        totalitem = 0
        wishitem = 0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
            wishitem = len(Wishlist.objects.filter(user = request.user))
        user = request.user
        add = Perfil.objects.filter(user = user)
        cart_items = Cart.objects.filter(user = user)
        famount = 0
        for p in cart_items:
            value = p.quantity * p.product.discounted_price
            famount = famount + value
        totalamount = famount + 40
        
        return render(request, 'app/checkout.html',locals())


@login_required
def plus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity+=1
        c.save()
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0
        for p in cart:
            value = p.quantity * p.product.discounted_price
            amount = amount + value
        totalamount = amount + 40
        totalamount = round(totalamount, 2)

        data={
            'quantity':c.quantity,
            'amount':amount,
            'totalamount':totalamount            
        }
        return JsonResponse(data)
    


@login_required    
def minus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity-=1
        c.save()
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0
        for p in cart:
            value = p.quantity * p.product.discounted_price
            amount = amount + value
        totalamount = amount + 40
        totalamount = round(totalamount, 2)

        data={
            'quantity':c.quantity,
            'amount':amount,
            'totalamount':totalamount            
        }
        return JsonResponse(data)


@login_required    
def remove_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.delete()
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0
        for p in cart:
            value = p.quantity * p.product.discounted_price
            amount = amount + value
        totalamount = amount + 40
        totalamount = round(totalamount, 2)

        data={
            'amount':amount,
            'totalamount':totalamount            
        }
        return JsonResponse(data)


@login_required    
def orders(request):
    order_placed = OrderPlaced.objects.filter(user= request.user)
    return render(request, 'app/orders.html', locals())


@login_required
def plus_wishlist(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        product = Product.objects.get(id=prod_id)
        user = request.user 
        Wishlist(user=user, product=product).save()
        data = {
            'message': 'Producto agregado a la lista de deseo correctamente',
        }
        return JsonResponse(data)
    

@login_required
def minus_wishlist(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        product = Product.objects.get(id = prod_id)
        user = request.user
        Wishlist.objects.filter(user=user, product=product).delete()
        data = {
            'message': 'Producto eliminado de la lista de deseos correctamente',
        }
        
        return JsonResponse(data)


@login_required
def search(request):
    query = request.GET.get('search')
    totalitem = 0
    wishitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
        wishitem = len(Wishlist.objects.filter(user = request.user))
    product = Product.objects.filter(Q(title__icontains=query))
    return render(request, 'app/search.html', locals())


@login_required
def pagar(request):
    totalitem = 0
    wishitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
        wishitem = len(Wishlist.objects.filter(user = request.user))
    return render(request, 'app/pago.html', locals())