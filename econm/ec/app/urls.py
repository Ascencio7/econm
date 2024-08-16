#Se importa "path" para definir mis rutas en mi app.
from django.urls import path
#Se importa el modulo "admin" para registrar y administrar modelos en el sitio de Django.
from django.contrib import admin
#Se importa las vistas de mi aplicación.
from . import views
#Se importa "settings y static" para usar archivos estáticos y multimedia.
from django.conf import settings
from django.conf.urls.static import static
#Se importa "auth_view" para vistas incorporadas de autenticación de Django.
from django.contrib.auth import views as auth_view
#Se importan mis formularios personalizados desde "forms.py"
from .forms import LoginForm, MyPasswordResetForm, MyPasswordChangeForm, MySetPasswordForm

#Aquí se definen todas mis rutas
urlpatterns = [
    path("", views.home),
    #Vista que muestra info sobre quiénes somos.
    path("about/", views.about, name="about"),
    #Vista para iniciar sesión.
    path("login/", views.home , name="login"),
    #Vista para los contactos directos de la página.
    path("contact/", views.contact, name="contact"),
    #Vista que muestra la categoría del producto en especifico.
    path("category/<slug:val>", views.CategoryView.as_view(), name="category"),
    #Vista que muestra el título de la categoría del producto en especifico.
    path("category-title/<val>", views.CategoryTitle.as_view(), name="category-title"),
    #Vista que muestra los detalles del producto.
    path("product-detail/<int:pk>", views.ProductDetail.as_view(), name="product-detail"),
    #Vista que muestra el perfil del usuario.
    path('profile/',views.ProfileView.as_view(), name='profile'),
    #Vista para agregar dirección del usuario.
    path('address/', views.address, name='address' ),
    #Vista para modificar la dirección.
    path('updateAddress/<int:pk>', views.updateAddress.as_view(), name='updateAddress'),
    
    #Vistas para poder pagar el producto
    path('add-to-cart/', views.add_to_cart, name='add-to-cart'),
    path('cart/', views.show_cart, name='showcart'),
    path('checkout/', views.checkout.as_view(), name='checkout'),
    path('pagar/', views.pagar, name='pagar'),
    path('orders/', views.orders, name='orders'),
    
    #Vista para agregar un producto como favorito.
    path('pluswishlist/', views.plus_wishlist),
    path('minuswishlist/', views.minus_wishlist),
    
    #Vista para buscar un producto en especial.
    path('search/', views.search, name='search'),
    
    #evento JS para aumentar, disminuir y eliminar la cantidad de un producto deseado.
    path('pluscart/', views.plus_cart),
    path('minuscart/', views.minus_cart),
    path('removecart/', views.remove_cart),
    
    #Iniciar el registro
    path('registration/', views.CustomerRegistrationView.as_view(), name='customerregistration'),
    path('accountslogin/', auth_view.LoginView.as_view(template_name='app/login.html', authentication_form=LoginForm), name='login'),
    path('passwordchange/', auth_view.PasswordChangeView.as_view(template_name='app/changepassword.html', form_class=MyPasswordChangeForm, success_url='/passwordchangedone'), name='passwordchange'),
    path('passwordchangedone/', auth_view.PasswordChangeDoneView.as_view(template_name='app/passwordchangedone.html'), name='passwordchangedone'),
    path('logout/', auth_view.LogoutView.as_view(next_page='login') , name='logout'),
    
    #Vistas para los eventos de las contraseñas.
    path('password-reset/', auth_view.PasswordResetView.as_view(template_name='app/password_reset.html', form_class=MyPasswordResetForm), name='password_reset'),
    path('password-reset/done/', auth_view.PasswordChangeDoneView.as_view(template_name='app/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_view.PasswordResetConfirmView.as_view(template_name='app/password_reset_confirm.html', form_class=MySetPasswordForm), name='password_reset_confirm'),
    path('password-reset-complete/', auth_view.PasswordResetCompleteView.as_view(template_name='app/password_reset_complete.html'), name='password_reset_complete'),
    
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

""" 
Este sirve para subir archivos media durante el desarrollo. 

1. settings.MEDIA.URL: Define la URL base para los archivos media.
2. settings.MEDIA_ROOT: Define la ruta raíz del directorio donde se almacenan los archivos media.

"""

#Cambio para el login de admin de DJANGO

admin.site.site_header = "VLADI STORE"
admin.site.site_title = "VLADI STORE"
admin.site.site_index_title = "Bienvenido a VLADI STORE"